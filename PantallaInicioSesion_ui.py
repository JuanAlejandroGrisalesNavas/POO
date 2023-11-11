# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PantallaInicioSesion.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QWidget)
import imagenes_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1450, 808)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet(u"background-color: rgb(10, 101, 112);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 0, 381, 381))
        self.label_2.setStyleSheet(u"image: url(:/Login/AdobeStock_621193540.png)")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(390, 0, 381, 381))
        self.label_4.setStyleSheet(u"image: url(:/Login/AdobeStock_621193540.png)")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(770, 380, 391, 391))
        self.label_5.setStyleSheet(u"image: url(:/Login/AdobeStock_621193540.png)")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(1150, 370, 381, 401))
        self.label_6.setStyleSheet(u"image: url(:/Login/AdobeStock_621193540.png)")
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(1150, 0, 381, 381))
        self.label_7.setStyleSheet(u"image: url(:/Login/AdobeStock_621193540.png)")
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(770, 0, 381, 381))
        self.label_8.setStyleSheet(u"image: url(:/Login/AdobeStock_621193540.png)")
        self.MostrarContra = QLabel(self.centralwidget)
        self.MostrarContra.setObjectName(u"MostrarContra")
        self.MostrarContra.setGeometry(QRect(570, 530, 141, 31))
        self.MostrarContra.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 75 15pt \"Yu Gothic UI Semibold\";")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(530, 540, 31, 21))
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"background-color: rgb(10, 101, 112)\n"
"font: 75 15pt \"Yu Gothic UI Semibold\";\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(255,255,255)\n"
"font: 75 15pt \"Yu Gothic UI Semibold\";\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(500, 370, 461, 41))
        self.lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;")
        self.lineEdit.setAlignment(Qt.AlignCenter)
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(510, 470, 451, 41))
        self.lineEdit_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;")
        self.lineEdit_2.setAlignment(Qt.AlignCenter)
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(520, 320, 71, 31))
        self.label_9.setStyleSheet(u"\n"
"color: rgb(255, 255, 255);\n"
"font: 75 15pt \"Yu Gothic UI Semibold\";\n"
"background-color: #000000ff;\n"
"")
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(0, 380, 391, 391))
        self.label_10.setStyleSheet(u"image: url(:/Login/AdobeStock_621193540.png)")
        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(390, 380, 391, 391))
        self.label_11.setStyleSheet(u"image: url(:/Login/AdobeStock_621193540.png)")
        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(520, 430, 101, 31))
        self.label_12.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 75 15pt \"Yu Gothic UI Semibold\";\n"
"background-color: #000000ff;\n"
"")
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(1320, 710, 91, 31))
        self.pushButton_3.setStyleSheet(u"\n"
"QFrame{\n"
"background-color: rgb(10, 101, 112);\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: #000000ff;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(100, 101, 112);\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(700, 600, 81, 31))
        self.pushButton.setStyleSheet(u"\n"
"QFrame{\n"
"background-color: rgb(10, 101, 112);\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(100, 101, 112);\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(255,255,255)\n"
"\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"")
        MainWindow.setCentralWidget(self.centralwidget)
        self.label_11.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_2.raise_()
        self.label_4.raise_()
        self.MostrarContra.raise_()
        self.pushButton_2.raise_()
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.label_12.raise_()
        self.pushButton_3.raise_()
        self.pushButton.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"PantallaInicioSesion", None))
        self.label_2.setText("")
        self.label_4.setText("")
        self.label_5.setText("")
        self.label_6.setText("")
        self.label_7.setText("")
        self.label_8.setText("")
        self.MostrarContra.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Mostrar contrase\u00f1a</span></p></body></html>", None))
        self.pushButton_2.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ingrese Usuario", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ingrese Contrase\u00f1a", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Usuario", None))
        self.label_10.setText("")
        self.label_11.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"SALIR", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"INGRESAR", None))
    # retranslateUi

