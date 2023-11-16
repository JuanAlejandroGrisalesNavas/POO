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
        self.MostrarContra = QLabel(self.centralwidget)
        self.MostrarContra.setObjectName(u"MostrarContra")
        self.MostrarContra.setGeometry(QRect(570, 530, 141, 31))
        self.MostrarContra.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 75 15pt \"Yu Gothic UI Semibold\";")
        self.Boton_mostrarContrasena = QPushButton(self.centralwidget)
        self.Boton_mostrarContrasena.setObjectName(u"Boton_mostrarContrasena")
        self.Boton_mostrarContrasena.setGeometry(QRect(530, 540, 31, 21))
        self.Boton_mostrarContrasena.setStyleSheet(u"QPushButton{\n"
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
        self.lineEdit_Ingrese_usuario = QLineEdit(self.centralwidget)
        self.lineEdit_Ingrese_usuario.setObjectName(u"lineEdit_Ingrese_usuario")
        self.lineEdit_Ingrese_usuario.setGeometry(QRect(500, 370, 461, 41))
        self.lineEdit_Ingrese_usuario.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;")
        self.lineEdit_Ingrese_usuario.setAlignment(Qt.AlignCenter)
        self.lineEdit_Ingrese_contrasena = QLineEdit(self.centralwidget)
        self.lineEdit_Ingrese_contrasena.setObjectName(u"lineEdit_Ingrese_contrasena")
        self.lineEdit_Ingrese_contrasena.setGeometry(QRect(510, 470, 451, 41))
        self.lineEdit_Ingrese_contrasena.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;")
        self.lineEdit_Ingrese_contrasena.setAlignment(Qt.AlignCenter)
        self.Boton_Salir = QPushButton(self.centralwidget)
        self.Boton_Salir.setObjectName(u"Boton_Salir")
        self.Boton_Salir.setGeometry(QRect(1320, 710, 91, 31))
        self.Boton_Salir.setStyleSheet(u"\n"
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
        self.Boton_ingresar = QPushButton(self.centralwidget)
        self.Boton_ingresar.setObjectName(u"Boton_ingresar")
        self.Boton_ingresar.setGeometry(QRect(700, 600, 81, 31))
        self.Boton_ingresar.setStyleSheet(u"\n"
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

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"PantallaInicioSesion", None))
        self.MostrarContra.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Mostrar contrase\u00f1a</span></p></body></html>", None))
        self.Boton_mostrarContrasena.setText("")
        self.lineEdit_Ingrese_usuario.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ingrese Usuario", None))
        self.lineEdit_Ingrese_contrasena.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ingrese Contrase\u00f1a", None))
        self.Boton_Salir.setText(QCoreApplication.translate("MainWindow", u"SALIR", None))
        self.Boton_ingresar.setText(QCoreApplication.translate("MainWindow", u"INGRESAR", None))
    # retranslateUi

