from PySide6.QtWidgets import QApplication, QFileDialog, QMainWindow
from PySide6.QtCore import QDir, QObject
import requests
from selectolax.parser import HTMLParser
from lxml import etree
import sys 
import gui
import time
import asyncio
import pandas as pd
import numpy as np
from aiolimiter import AsyncLimiter


class Main(QMainWindow, gui.Ui_MainWindow):
    def __init__(self, parent=None):
        # super(Main, self).__init__(parent)
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Web Scraper")

        # Exit button
        self.exit_btn.clicked.connect(self.exit_script)

        # Fetch links button trigger
        self.fetch_text.setText("")
        self.fetch_btn.clicked.connect(self.fetch_links_script)

        # Create a status bar
        self.statusBar().showMessage("Ready")

        # Search button trigger
        self.search_btn.clicked.connect(self.search_query)

        # Sync mode radio button
        self.get_data_btn.clicked.connect(self.get_data)

        # Max_rate spinbox value
        self.max_rate_spinbox.setRange(1, 1000)
        self.max_rate_spinbox.setValue(100)
        self.max_rate_spinbox.valueChanged.connect(self.max_rate_spinbox_change)

        # time_sec spinbox value
        self.time_spinbox.setRange(1, 60)
        self.time_spinbox.setValue(1)
        self.time_spinbox.valueChanged.connect(self.time_spinbox_change)

        # Output directory button
        # self.output_btn.clicked.connect(self.output_directory)

   
    def fetch_links_script(self):
        '''
        Extract list of all url, last modified date and update frequency from sitemap.
        '''
        url = 'https://www.blake-uk.com/sitemap.xml'

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246'
        }
        try:
            response = requests.get(url, headers=headers)
            tree = etree.fromstring(response.content)
            result = []
            for url in tree.findall('{http://www.sitemaps.org/schemas/sitemap/0.9}url'):
                loc = url.find('{http://www.sitemaps.org/schemas/sitemap/0.9}loc').text
                if loc.endswith('.html'):
                    data = {
                        'url': loc,
                        'lastmod': url.find('{http://www.sitemaps.org/schemas/sitemap/0.9}lastmod').text,
                        'freq': url.find('{http://www.sitemaps.org/schemas/sitemap/0.9}changefreq').text
                    }
                    result.append(data)
            self.fetch_text.setText(f'Links fetched: {len(result):,}')
            self.statusBar().showMessage(f'Total {len(result):,} links.')
            links = [x['url'] for x in result]
            return links
        except (requests.exceptions.RequestException or requests.exceptions.ReadTimeout or requests.exceptions.HTTPError) as e:
            self.fetch_text.setText(f'Error: {e}')

    async def async_mode_script(self):
        await self.scrape_urls()

    def search_query(self):
        query = self.search_text.text()
        if (query == "") or (query is None):
            self.urls = self.fetch_links_script()
        else:
            self.urls = [item for item in self.fetch_links_script() if str(query).lower() in item]
        self.search_link_script(query, self.urls)

    def search_link_script(self, query, urls):
        self.statusBar().showMessage(f'There are {len(urls):,} {query} links available.')

    def exit_script(self):
        self.close()

    async def fetch_url(self, url, limiter):
        async with limiter:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246'}
            try:
                with requests.Session() as session:
                    response = await asyncio.to_thread(session.get, url, headers=headers)
                    site = HTMLParser(response.text)
                    product_specs = self.product_specification(site)
                    product_tech = self.technical_specification(site)
                    data = dict(
                        product_name="" if site.css_first(
                            '.js-product-name.js-product-title') is None else site.css_first(
                            '.js-product-name.js-product-title').text(strip=True),
                        product_code="" if site.css_first('span.js-product-stock-code') is None else site.css_first(
                            'span.js-product-stock-code').text(strip=True),
                        price_incvat="" if site.css_first('.price.incvat') is None else site.css_first(
                            '.price.incvat').text(strip=True, deep=False),
                        price_excvat="" if site.css_first('.price.excvat') is None else site.css_first(
                            '.price.excvat').text(strip=True, deep=False),
                        product_url=url,
                        images=[x.attributes.get('src') for x in site.css('.product-page__slideshow img[src]')],
                        stock_status="" if site.css_first('.guarantees__list:first-child') is None else site.css_first(
                            '.guarantees__list:first-child').text(strip=True, deep=False),
                        product_features=[x.text(strip=True, deep=False) for x in site.css('.product-page__info li')],
                        product_specification="" if product_specs is None else product_specs,
                        technical_specification="" if product_tech is None else product_tech
                    )
                    return data
            except (
                    requests.exceptions.RequestException or requests.exceptions.ReadTimeout or requests.exceptions.HTTPError) as e:
                self.statusBar().showMessage(f'Error: {e}')

    def product_specification(self, site):
        table = site.css_first('.product-page__table:first-of-type')
        if table is None:
            return {}
        rows = table.css('tr')
       
        result = []
        for row in rows:
            cols = row.css('td') or row.css('th')
            cols = [col.text(deep=True).strip() for col in cols]
            result.append(cols)
        # headers = result[0]
        # data= {headers[i]: [row[i] for row in result[1:] if len(row) > i] for i in range(len(headers))}
        # return data

        # IndexError: list index out of range with headers
        if len(result) > 0:
            headers = result[0]
            data = {headers[i]: [row[i] for row in result[1:] if len(row) > i] for i in range(len(headers)) if i < len(headers)}
            return data
        else:
            return None

    def technical_specification(self, site):
        # Find all the list items
        rows = site.css('div.product-page__list')
        if rows is None:
            return []

        output = []
        for row in rows:
            item = [x.text().strip() for x in row.css('.product-page__list p:nth-child(2)')]
            value = [x.text().strip() for x in row.css('.product-page__list p:nth-child(1)')]
            d = {item[i]: value[i] for i in range(len(item))}
            output.append(d)
        return {k: v for i in output for k,v in i.items()}
                
    def max_rate_spinbox_change(self, value):
        self.max_rate_spinbox.setValue(value)

    def time_spinbox_change(self, value):
        self.time_spinbox.setValue(value)

    async def scrape_urls(self):
        max_rate = self.max_rate_spinbox.value()
        time_sec = self.time_spinbox.value()
        rate_limiter = AsyncLimiter(max_rate, time_sec)
        tasks = []
        for url in self.urls:
            tasks.append(asyncio.create_task(self.fetch_url(url, rate_limiter)))
        result = await asyncio.gather(*tasks)
        output = [item for item in result if item is not None]
        data = {
            key: [d.get(key) for d in output]
            for key in set().union(*output)
        }
        self.statusBar().showMessage(f'Scraped {len(self.urls)} links.')
        self.excel_export(output, data)

    def get_data(self):
        asyncio.run(self.scrape_urls())

    def excel_export(self, output, data):
        current_time = time.localtime()
        formatted_time = time.strftime('%d-%m-%y', current_time)
        writer = pd.ExcelWriter(f'output-{formatted_time}.xlsx', engine='xlsxwriter')
        df = pd.DataFrame(output)
        df = df.replace("", np.nan).dropna(axis='rows', how='any')
        df.to_excel(writer, sheet_name='summary', index=False)
        df_e = df.explode('images')
        df_e = df_e.explode('product_features')
        df_e = df_e.loc[:, 'product_name':'product_features']
        df_e.to_excel(writer, sheet_name='Expanded', index=False)

        # Product specification and technical specification
        output = []
        key = ['product_name', 'product_code', 'product_url', 'technical_specification']
        for i in key:
            d = pd.DataFrame(data[i]).rename(columns={0: i})
            output.append(d)
        df_prod = pd.concat(output, axis='columns').dropna(axis='rows', how='all')
        df_g = []
        for i in data['product_specification']:
            if isinstance(i, dict):
                df = pd.DataFrame.from_dict(i, orient='index').replace("", np.nan).ffill(axis='rows').T
            else:
                pass
            df_g.append(df)
        df_spec = pd.concat(df_g, axis='rows').dropna(axis='rows', how='all').drop_duplicates()

        # Merge dataframes
        if ('Product Code' or 'Product') in df_spec.columns:
            df_merge = df_prod.merge(df_spec, left_on='product_code', right_on=['Product Code' or 'Product'], how='left')
        else:
            df_merge = df_spec
        df_merge.to_excel(writer, sheet_name="product_details", index=False)
        writer.close()
        self.statusBar().showMessage("Links fetched and converted to Excel file.")


def main():
    if not QApplication.instance():
        app = QApplication(sys.argv)
    else:
        app = QApplication.instance()
    form = Main()
    form.show()
    app.exec()


if __name__ == '__main__':
    main()
