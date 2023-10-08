# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'blakev1jBAPAY.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpinBox, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(300, 295)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 6, 281, 51))
        self.fetch_btn = QPushButton(self.groupBox_2)
        self.fetch_btn.setObjectName(u"fetch_btn")
        self.fetch_btn.setGeometry(QRect(10, 18, 75, 24))
        self.fetch_text = QLabel(self.groupBox_2)
        self.fetch_text.setObjectName(u"fetch_text")
        self.fetch_text.setGeometry(QRect(100, 18, 171, 20))
        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(10, 64, 281, 51))
        self.search_btn = QPushButton(self.groupBox_3)
        self.search_btn.setObjectName(u"search_btn")
        self.search_btn.setGeometry(QRect(10, 18, 75, 24))
        self.search_text = QLineEdit(self.groupBox_3)
        self.search_text.setObjectName(u"search_text")
        self.search_text.setGeometry(QRect(90, 19, 181, 21))
        self.groupBox_6 = QGroupBox(self.centralwidget)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setGeometry(QRect(10, 176, 281, 51))
        self.get_data_btn = QPushButton(self.groupBox_6)
        self.get_data_btn.setObjectName(u"get_data_btn")
        self.get_data_btn.setGeometry(QRect(10, 19, 261, 24))
        self.exit_btn = QPushButton(self.centralwidget)
        self.exit_btn.setObjectName(u"exit_btn")
        self.exit_btn.setGeometry(QRect(20, 234, 75, 24))
        self.groupBox_4 = QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(11, 116, 281, 51))
        self.max_rate_label = QLabel(self.groupBox_4)
        self.max_rate_label.setObjectName(u"max_rate_label")
        self.max_rate_label.setGeometry(QRect(11, 23, 51, 16))
        self.time = QLabel(self.groupBox_4)
        self.time.setObjectName(u"time")
        self.time.setGeometry(QRect(162, 24, 51, 16))
        self.max_rate_spinbox = QSpinBox(self.groupBox_4)
        self.max_rate_spinbox.setObjectName(u"max_rate_spinbox")
        self.max_rate_spinbox.setGeometry(QRect(66, 20, 51, 22))
        self.time_spinbox = QSpinBox(self.groupBox_4)
        self.time_spinbox.setObjectName(u"time_spinbox")
        self.time_spinbox.setGeometry(QRect(220, 20, 51, 22))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 300, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Step 1: Fetch links", None))
        self.fetch_btn.setText(QCoreApplication.translate("MainWindow", u"Fetch", None))
        self.fetch_text.setText(QCoreApplication.translate("MainWindow", u"fetch_link_status", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Step 2: Search specific product", None))
        self.search_btn.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Step 4: Getting data from website", None))
        self.get_data_btn.setText(QCoreApplication.translate("MainWindow", u"Get data", None))
        self.exit_btn.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Step 3: Limiter", None))
        self.max_rate_label.setText(QCoreApplication.translate("MainWindow", u"Max rate", None))
        self.time.setText(QCoreApplication.translate("MainWindow", u"Time(sec)", None))
    # retranslateUi

