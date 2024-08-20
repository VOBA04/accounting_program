# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QMainWindow,
    QMenuBar, QPushButton, QScrollArea, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        icon = QIcon(QIcon.fromTheme(u"emblem-documents"))
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 40))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_addKiosk = QPushButton(self.widget)
        self.pushButton_addKiosk.setObjectName(u"pushButton_addKiosk")

        self.horizontalLayout.addWidget(self.pushButton_addKiosk)

        self.pushButton_addKiosks = QPushButton(self.widget)
        self.pushButton_addKiosks.setObjectName(u"pushButton_addKiosks")

        self.horizontalLayout.addWidget(self.pushButton_addKiosks)

        self.pushButton_deleteKiosk = QPushButton(self.widget)
        self.pushButton_deleteKiosk.setObjectName(u"pushButton_deleteKiosk")

        self.horizontalLayout.addWidget(self.pushButton_deleteKiosk)

        self.pushButton_itemWindow = QPushButton(self.widget)
        self.pushButton_itemWindow.setObjectName(u"pushButton_itemWindow")

        self.horizontalLayout.addWidget(self.pushButton_itemWindow)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 780, 491))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 20))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0423\u0447\u0435\u0442 \u041c\u0411\u041f", None))
        self.pushButton_addKiosk.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_addKiosks.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_deleteKiosk.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_itemWindow.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
    # retranslateUi

