# Blake-uk.com Web Scraper

![Python](https://img.shields.io/badge/Python-3.7%2B-blue)
![Dependencies](https://img.shields.io/badge/Dependencies-PySide6%2C%20Requests%2C%20lxml%2C%20selectolax%2C%20aiolimiter%2C%20Pandas%2C%20XlsxWriter-brightgreen)

## Project Description

The **Blake-uk.com Web Scraper** is a Python GUI application designed for efficiently scraping data from [Blake-uk.com](https://www.blake-uk.com/), a prominent online resource. This application is built using a powerful stack of dependencies, including PySide6 for creating a user-friendly graphical interface, Requests for handling HTTP requests, lxml for parsing XML, selectolax for efficient HTML parsing, aiolimiter for rate limiting, Pandas and XlsxWriter for data manipulation and export to excel.

![1](https://github.com/kashifnaz/Blake-uk.com_Web_Scraper/assets/39775989/d3d7ee7c-64c2-4359-8f47-e6e7d938f485)

### Key Features

- **Asynchronous Web Scraping**: This application harnesses the power of the asyncio library, enabling asynchronous web scraping for exceptionally fast data retrieval. Asynchronous operations allow for multiple web requests to be processed simultaneously, resulting in improved efficiency.

- **Sitemap-Based URL Discovery**: The scraper starts its data collection process by reading the website's sitemap, automatically discovering and processing all relevant URLs. This approach ensures a comprehensive and systematic data extraction process.

- **Efficient HTML Parsing**: The project employs the Selectolax library for HTML parsing. Selectolax is known for its efficiency, making it an excellent choice for extracting structured data from web pages.

- **Search Capability**: The application offers a robust search feature that allows users to specify criteria for extracting particular product data. This capability makes it versatile for various data extraction needs.

- **Rate Limiting with aiolimiter**: To maintain server-friendly behavior, the application utilizes aiolimiter for rate limiting. This ensures that requests to the server are controlled without causing blocking, allowing for smooth and responsible scraping.

- **Data Output**: After scraping, the application exports the collected data to separate Excel sheets, namely "summary," "expanded," and "product details." This organized data format facilitates further analysis and reference.

## Getting Started

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/yourusername/blake-uk-web-scraper.git
   cd blake-uk-web-scraper
   ```

2. **Install Dependencies**:

   Use `pip` to install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**:

   Execute the Python script to launch the GUI application:

   ```bash
   python main.py
   ```
4. **Start Scraping**:

   Use the intuitive user interface to configure your scraping preferences and initiate the data extraction process.

## Example Output

This application generates an Excel file containing the following output, with the file name based on the date when the data was scraped.

![2](https://github.com/kashifnaz/Blake-uk.com_Web_Scraper/assets/39775989/526874a9-54af-44fb-a8be-b15c08341fdc)

![3](https://github.com/kashifnaz/Blake-uk.com_Web_Scraper/assets/39775989/12b02c1b-4dff-46a5-a58f-0923a3fdb68f)
   
## Contributions

Contributions to this project are welcome! If you find any issues or have ideas for improvements, please submit an issue or a pull request on GitHub.

## Disclaimer

This application is intended for educational and informational purposes only. Please be mindful and responsible when using web scraping tools. Always review and comply with the website's terms of service and policies.

## License

This project is licensed under the MIT License. For detailed information, refer to the [LICENSE](LICENSE) file.
