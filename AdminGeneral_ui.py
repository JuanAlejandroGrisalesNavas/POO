# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AdminGeneral.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1458, 825)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(10, 101, 112);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_superior = QFrame(self.frame)
        self.frame_superior.setObjectName(u"frame_superior")
        self.frame_superior.setMinimumSize(QSize(0, 42))
        self.frame_superior.setStyleSheet(u"QFrame{\n"
"background-color: rgb(10, 101, 112);\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: #000000ff;\n"
"border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(61,61,61);\n"
"border-radius: 20px;\n"
"}\n"
"\n"
"")
        self.frame_superior.setFrameShape(QFrame.StyledPanel)
        self.frame_superior.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_superior)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Boton_menu = QPushButton(self.frame_superior)
        self.Boton_menu.setObjectName(u"Boton_menu")
        self.Boton_menu.setMinimumSize(QSize(300, 0))
        icon = QIcon()
        icon.addFile(u"../Imagenes/menu (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.Boton_menu.setIcon(icon)
        self.Boton_menu.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.Boton_menu)

        self.horizontalSpacer = QSpacerItem(943, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.Boton_minimizar = QPushButton(self.frame_superior)
        self.Boton_minimizar.setObjectName(u"Boton_minimizar")
        self.Boton_minimizar.setMinimumSize(QSize(40, 40))
        icon1 = QIcon()
        icon1.addFile(u"../Imagenes/minimizar-signo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Boton_minimizar.setIcon(icon1)
        self.Boton_minimizar.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.Boton_minimizar)

        self.Boton_restaurar = QPushButton(self.frame_superior)
        self.Boton_restaurar.setObjectName(u"Boton_restaurar")
        self.Boton_restaurar.setMinimumSize(QSize(40, 40))
        icon2 = QIcon()
        icon2.addFile(u"../Imagenes/minimizar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Boton_restaurar.setIcon(icon2)
        self.Boton_restaurar.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.Boton_restaurar)

        self.Boton_maximizar = QPushButton(self.frame_superior)
        self.Boton_maximizar.setObjectName(u"Boton_maximizar")
        self.Boton_maximizar.setMinimumSize(QSize(40, 40))
        icon3 = QIcon()
        icon3.addFile(u"../Imagenes/maximizar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Boton_maximizar.setIcon(icon3)
        self.Boton_maximizar.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.Boton_maximizar)

        self.Boton_cerrar = QPushButton(self.frame_superior)
        self.Boton_cerrar.setObjectName(u"Boton_cerrar")
        self.Boton_cerrar.setMinimumSize(QSize(40, 40))
        icon4 = QIcon()
        icon4.addFile(u"../Imagenes/cerrar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Boton_cerrar.setIcon(icon4)
        self.Boton_cerrar.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.Boton_cerrar)


        self.verticalLayout_2.addWidget(self.frame_superior)

        self.frame_inferior = QFrame(self.frame)
        self.frame_inferior.setObjectName(u"frame_inferior")
        self.frame_inferior.setFrameShape(QFrame.StyledPanel)
        self.frame_inferior.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_inferior)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_control = QFrame(self.frame_inferior)
        self.frame_control.setObjectName(u"frame_control")
        self.frame_control.setMinimumSize(QSize(300, 0))
        self.frame_control.setMaximumSize(QSize(0, 16777215))
        self.frame_control.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
"	background-color: rgb(61, 61, 61);\n"
"	border-top-left-radius: 20px;\n"
"	border-bottom-left-radius: 20px;\n"
"	color: rgb(230,230,230);\n"
"	font: 75 15pt \"Yu Gothic UI Semibold\";\n"
"}\n"
"\n"
"QpushButtom: hover{\n"
"	background-color: black;\n"
"	border-top-left-radius: 20px;\n"
"	border-bottom-left-radius: 20px;\n"
"	color: rgb(255,255,255);\n"
"	font: 75 15pt \"Yu Gothic UI Semibold\";\n"
"}\n"
"\n"
"")
        self.frame_control.setFrameShape(QFrame.StyledPanel)
        self.frame_control.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_control)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.Boton_usuarios = QPushButton(self.frame_control)
        self.Boton_usuarios.setObjectName(u"Boton_usuarios")
        self.Boton_usuarios.setMinimumSize(QSize(0, 40))
        self.Boton_usuarios.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.Boton_usuarios)

        self.Boton_locales = QPushButton(self.frame_control)
        self.Boton_locales.setObjectName(u"Boton_locales")
        self.Boton_locales.setMinimumSize(QSize(0, 40))
        self.Boton_locales.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.Boton_locales)

        self.Boton_resumenVentas = QPushButton(self.frame_control)
        self.Boton_resumenVentas.setObjectName(u"Boton_resumenVentas")
        self.Boton_resumenVentas.setMinimumSize(QSize(0, 40))
        self.Boton_resumenVentas.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.Boton_resumenVentas)

        self.Boton_pedidos = QPushButton(self.frame_control)
        self.Boton_pedidos.setObjectName(u"Boton_pedidos")
        self.Boton_pedidos.setMinimumSize(QSize(0, 40))
        self.Boton_pedidos.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.Boton_pedidos)

        self.Boton_mesas = QPushButton(self.frame_control)
        self.Boton_mesas.setObjectName(u"Boton_mesas")
        self.Boton_mesas.setMinimumSize(QSize(0, 40))
        self.Boton_mesas.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.Boton_mesas)

        self.Boton_cerrarAbrirDia = QPushButton(self.frame_control)
        self.Boton_cerrarAbrirDia.setObjectName(u"Boton_cerrarAbrirDia")
        self.Boton_cerrarAbrirDia.setMinimumSize(QSize(0, 40))
        self.Boton_cerrarAbrirDia.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.Boton_cerrarAbrirDia)

        self.Boton_cerrarSesion = QPushButton(self.frame_control)
        self.Boton_cerrarSesion.setObjectName(u"Boton_cerrarSesion")
        self.Boton_cerrarSesion.setMinimumSize(QSize(0, 40))
        self.Boton_cerrarSesion.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.Boton_cerrarSesion)


        self.horizontalLayout_2.addWidget(self.frame_control)

        self.frame_contenido = QFrame(self.frame_inferior)
        self.frame_contenido.setObjectName(u"frame_contenido")
        self.frame_contenido.setStyleSheet(u"QFrame{\n"
"background-color: rgb(61,61,61);\n"
"}\n"
"\n"
"QLabel{\n"
"font: 75 15pt \"Yu Gothic UI Semibold\";\n"
"background-color: #000000ff;\n"
"color:rgb(0,206,151);\n"
"border:0px solid#14C8DC;\n"
"}\n"
"\n"
"QLineEdit{\n"
"border:0px;\n"
"color: rgb(0,0,0);\n"
"border-bottom:2px solid rgb(61,61,61);\n"
"font: 75 15pt \"Yu Gothic UI Semibold\";\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(61,61,61);\n"
"border-radius: 15px;\n"
"color:  rgb(0,0,0);\n"
"font: 75 15pt \"Yu Gothic UI Semibold\";\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 206, 151);\n"
"border-radius: 15px;\n"
"color:  rgb(230,230,230);\n"
"font: 75 15pt \"Yu Gothic UI Semibold\";\n"
"}\n"
"\n"
"QTableWidget{\n"
"background-color: rgb(130,130,130);\n"
"color:  rgb(230,230,230);\n"
"grindline-color: rgb(0, 206, 151);\n"
"font-size: 12pt;\n"
"color: #000000;\n"
"}\n"
"\n"
"QHeaderView::section{\n"
"background-color: rgb(0, 206, 151);\n"
"border:1px solid rgb(0,0,0);\n"
"font-size: 12pt;\n"
"}\n"
"\n"
"QTableWindget"
                        " QTableCornerButtom::section{\n"
"background-color: rgb(130,130,130);\n"
"color:  rgb(0, 206, 151);\n"
"}\n"
"")
        self.frame_contenido.setFrameShape(QFrame.StyledPanel)
        self.frame_contenido.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_contenido)
        self.verticalLayout_4.setSpacing(1)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(1, 1, 1, 1)
        self.stacked_Menu = QStackedWidget(self.frame_contenido)
        self.stacked_Menu.setObjectName(u"stacked_Menu")
        self.pagina_usuarios = QWidget()
        self.pagina_usuarios.setObjectName(u"pagina_usuarios")
        self.stacked_PaginaUuario = QStackedWidget(self.pagina_usuarios)
        self.stacked_PaginaUuario.setObjectName(u"stacked_PaginaUuario")
        self.stacked_PaginaUuario.setGeometry(QRect(10, 110, 1111, 601))
        self.Pagina_AgregarUsuario = QWidget()
        self.Pagina_AgregarUsuario.setObjectName(u"Pagina_AgregarUsuario")
        self.verticalLayout_8 = QVBoxLayout(self.Pagina_AgregarUsuario)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_5 = QLabel(self.Pagina_AgregarUsuario)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_5)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(30)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_7 = QLabel(self.Pagina_AgregarUsuario)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_7.addWidget(self.label_7)

        self.label_2 = QLabel(self.Pagina_AgregarUsuario)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_7.addWidget(self.label_2)

        self.label_3 = QLabel(self.Pagina_AgregarUsuario)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_7.addWidget(self.label_3)

        self.label_4 = QLabel(self.Pagina_AgregarUsuario)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_7.addWidget(self.label_4)


        self.horizontalLayout_5.addLayout(self.verticalLayout_7)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(30)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.lineEdit_4 = QLineEdit(self.Pagina_AgregarUsuario)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.verticalLayout_6.addWidget(self.lineEdit_4)

        self.lineEdit = QLineEdit(self.Pagina_AgregarUsuario)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout_6.addWidget(self.lineEdit)

        self.lineEdit_2 = QLineEdit(self.Pagina_AgregarUsuario)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.verticalLayout_6.addWidget(self.lineEdit_2)

        self.lineEdit_3 = QLineEdit(self.Pagina_AgregarUsuario)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.verticalLayout_6.addWidget(self.lineEdit_3)


        self.horizontalLayout_5.addLayout(self.verticalLayout_6)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)


        self.verticalLayout_8.addLayout(self.horizontalLayout_5)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_2)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_6 = QLabel(self.Pagina_AgregarUsuario)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(200, 0))
        self.label_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_6)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)

        self.pushButton = QPushButton(self.Pagina_AgregarUsuario)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_6.addWidget(self.pushButton)


        self.verticalLayout_8.addLayout(self.horizontalLayout_6)

        self.stacked_PaginaUuario.addWidget(self.Pagina_AgregarUsuario)
        self.Pagina_EliminarUsuario = QWidget()
        self.Pagina_EliminarUsuario.setObjectName(u"Pagina_EliminarUsuario")
        self.verticalLayout_12 = QVBoxLayout(self.Pagina_EliminarUsuario)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_16 = QLabel(self.Pagina_EliminarUsuario)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_16)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_17 = QLabel(self.Pagina_EliminarUsuario)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_10.addWidget(self.label_17)

        self.lineEdit_11 = QLineEdit(self.Pagina_EliminarUsuario)
        self.lineEdit_11.setObjectName(u"lineEdit_11")

        self.horizontalLayout_10.addWidget(self.lineEdit_11)

        self.pushButton_4 = QPushButton(self.Pagina_EliminarUsuario)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_10.addWidget(self.pushButton_4)


        self.verticalLayout_12.addLayout(self.horizontalLayout_10)

        self.tableWidget = QTableWidget(self.Pagina_EliminarUsuario)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout_12.addWidget(self.tableWidget)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_18 = QLabel(self.Pagina_EliminarUsuario)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(200, 30))

        self.horizontalLayout_11.addWidget(self.label_18)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_7)

        self.pushButton_5 = QPushButton(self.Pagina_EliminarUsuario)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(120, 30))

        self.horizontalLayout_11.addWidget(self.pushButton_5)


        self.verticalLayout_12.addLayout(self.horizontalLayout_11)

        self.stacked_PaginaUuario.addWidget(self.Pagina_EliminarUsuario)
        self.Pagina_ModificarUsuario = QWidget()
        self.Pagina_ModificarUsuario.setObjectName(u"Pagina_ModificarUsuario")
        self.verticalLayout_11 = QVBoxLayout(self.Pagina_ModificarUsuario)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_15 = QLabel(self.Pagina_ModificarUsuario)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_15)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_8 = QLabel(self.Pagina_ModificarUsuario)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_9.addWidget(self.label_8)

        self.lineEdit_5 = QLineEdit(self.Pagina_ModificarUsuario)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.horizontalLayout_9.addWidget(self.lineEdit_5)

        self.pushButton_3 = QPushButton(self.Pagina_ModificarUsuario)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout_9.addWidget(self.pushButton_3)


        self.verticalLayout_11.addLayout(self.horizontalLayout_9)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_4)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_9 = QLabel(self.Pagina_ModificarUsuario)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_10.addWidget(self.label_9)

        self.label_10 = QLabel(self.Pagina_ModificarUsuario)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_10.addWidget(self.label_10)

        self.label_11 = QLabel(self.Pagina_ModificarUsuario)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_10.addWidget(self.label_11)

        self.label_12 = QLabel(self.Pagina_ModificarUsuario)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_10.addWidget(self.label_12)

        self.label_13 = QLabel(self.Pagina_ModificarUsuario)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_10.addWidget(self.label_13)


        self.horizontalLayout_8.addLayout(self.verticalLayout_10)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setSpacing(30)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.lineEdit_6 = QLineEdit(self.Pagina_ModificarUsuario)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.verticalLayout_9.addWidget(self.lineEdit_6)

        self.lineEdit_7 = QLineEdit(self.Pagina_ModificarUsuario)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.verticalLayout_9.addWidget(self.lineEdit_7)

        self.lineEdit_8 = QLineEdit(self.Pagina_ModificarUsuario)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.verticalLayout_9.addWidget(self.lineEdit_8)

        self.lineEdit_9 = QLineEdit(self.Pagina_ModificarUsuario)
        self.lineEdit_9.setObjectName(u"lineEdit_9")

        self.verticalLayout_9.addWidget(self.lineEdit_9)

        self.lineEdit_10 = QLineEdit(self.Pagina_ModificarUsuario)
        self.lineEdit_10.setObjectName(u"lineEdit_10")

        self.verticalLayout_9.addWidget(self.lineEdit_10)


        self.horizontalLayout_8.addLayout(self.verticalLayout_9)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_6)


        self.verticalLayout_11.addLayout(self.horizontalLayout_8)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_3)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_14 = QLabel(self.Pagina_ModificarUsuario)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(0, 50))

        self.horizontalLayout_7.addWidget(self.label_14)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_5)

        self.pushButton_2 = QPushButton(self.Pagina_ModificarUsuario)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_7.addWidget(self.pushButton_2)


        self.verticalLayout_11.addLayout(self.horizontalLayout_7)

        self.stacked_PaginaUuario.addWidget(self.Pagina_ModificarUsuario)
        self.widget = QWidget(self.pagina_usuarios)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(290, 10, 511, 98))
        self.horizontalLayout_4 = QHBoxLayout(self.widget)
        self.horizontalLayout_4.setSpacing(19)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(9, 9, 9, 9)
        self.Boton_AgregarUsuario = QPushButton(self.widget)
        self.Boton_AgregarUsuario.setObjectName(u"Boton_AgregarUsuario")
        self.Boton_AgregarUsuario.setMinimumSize(QSize(80, 40))

        self.horizontalLayout_4.addWidget(self.Boton_AgregarUsuario)

        self.Boton_ModificaUsuario = QPushButton(self.widget)
        self.Boton_ModificaUsuario.setObjectName(u"Boton_ModificaUsuario")
        self.Boton_ModificaUsuario.setMinimumSize(QSize(80, 40))

        self.horizontalLayout_4.addWidget(self.Boton_ModificaUsuario)

        self.Boton_EliminarUsuario = QPushButton(self.widget)
        self.Boton_EliminarUsuario.setObjectName(u"Boton_EliminarUsuario")
        self.Boton_EliminarUsuario.setMinimumSize(QSize(80, 40))
        self.Boton_EliminarUsuario.setMaximumSize(QSize(300, 16777215))

        self.horizontalLayout_4.addWidget(self.Boton_EliminarUsuario)

        self.stacked_Menu.addWidget(self.pagina_usuarios)
        self.pagina_ResumenV = QWidget()
        self.pagina_ResumenV.setObjectName(u"pagina_ResumenV")
        self.verticalLayout_5 = QVBoxLayout(self.pagina_ResumenV)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label = QLabel(self.pagina_ResumenV)
        self.label.setObjectName(u"label")
        self.label.setFrameShadow(QFrame.Plain)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label)

        self.Tabla_basedatos = QTableWidget(self.pagina_ResumenV)
        if (self.Tabla_basedatos.columnCount() < 5):
            self.Tabla_basedatos.setColumnCount(5)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.Tabla_basedatos.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.Tabla_basedatos.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.Tabla_basedatos.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.Tabla_basedatos.setHorizontalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.Tabla_basedatos.setHorizontalHeaderItem(4, __qtablewidgetitem8)
        self.Tabla_basedatos.setObjectName(u"Tabla_basedatos")

        self.verticalLayout_5.addWidget(self.Tabla_basedatos)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.Boton_ActualizarBase = QPushButton(self.pagina_ResumenV)
        self.Boton_ActualizarBase.setObjectName(u"Boton_ActualizarBase")
        self.Boton_ActualizarBase.setMinimumSize(QSize(30, 40))

        self.horizontalLayout_3.addWidget(self.Boton_ActualizarBase)


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.stacked_Menu.addWidget(self.pagina_ResumenV)
        self.Pagina_Pedidos = QWidget()
        self.Pagina_Pedidos.setObjectName(u"Pagina_Pedidos")
        self.stacked_Menu.addWidget(self.Pagina_Pedidos)
        self.Pagina_Mesas = QWidget()
        self.Pagina_Mesas.setObjectName(u"Pagina_Mesas")
        self.stacked_Menu.addWidget(self.Pagina_Mesas)
        self.Pagina_AbrirCerrarDia = QWidget()
        self.Pagina_AbrirCerrarDia.setObjectName(u"Pagina_AbrirCerrarDia")
        self.stacked_Menu.addWidget(self.Pagina_AbrirCerrarDia)
        self.Pagina_cerrarSesion = QWidget()
        self.Pagina_cerrarSesion.setObjectName(u"Pagina_cerrarSesion")
        self.stacked_Menu.addWidget(self.Pagina_cerrarSesion)
        self.pagina_locales = QWidget()
        self.pagina_locales.setObjectName(u"pagina_locales")
        self.stacked_Menu.addWidget(self.pagina_locales)

        self.verticalLayout_4.addWidget(self.stacked_Menu)


        self.horizontalLayout_2.addWidget(self.frame_contenido)


        self.verticalLayout_2.addWidget(self.frame_inferior)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 9)

        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stacked_Menu.setCurrentIndex(0)
        self.stacked_PaginaUuario.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Boton_menu.setText("")
        self.Boton_minimizar.setText("")
        self.Boton_restaurar.setText("")
        self.Boton_maximizar.setText("")
        self.Boton_cerrar.setText("")
        self.Boton_usuarios.setText(QCoreApplication.translate("MainWindow", u"Usuarios", None))
        self.Boton_locales.setText(QCoreApplication.translate("MainWindow", u"Locales", None))
        self.Boton_resumenVentas.setText(QCoreApplication.translate("MainWindow", u"Resumen Ventas", None))
        self.Boton_pedidos.setText(QCoreApplication.translate("MainWindow", u"Pedidos", None))
        self.Boton_mesas.setText(QCoreApplication.translate("MainWindow", u"Mesas", None))
        self.Boton_cerrarAbrirDia.setText(QCoreApplication.translate("MainWindow", u"Abrir/Cerrar Dia", None))
        self.Boton_cerrarSesion.setText(QCoreApplication.translate("MainWindow", u"Cerrar Sesion", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"AGREGAR PRODUCTOS", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_6.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"ELIMINAR USUARIO", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"NOMBRE", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"BUSCAR", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Nombre", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Producto", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Contrasena", None));
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"ELIMINAR", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"MODIFICAR USUARIO", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_14.setText("")
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.Boton_AgregarUsuario.setText(QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.Boton_ModificaUsuario.setText(QCoreApplication.translate("MainWindow", u"Modificar", None))
        self.Boton_EliminarUsuario.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"PRODUCTOS", None))
        ___qtablewidgetitem3 = self.Tabla_basedatos.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Producto", None));
        ___qtablewidgetitem4 = self.Tabla_basedatos.horizontalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Local", None));
        ___qtablewidgetitem5 = self.Tabla_basedatos.horizontalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Cantidad", None));
        ___qtablewidgetitem6 = self.Tabla_basedatos.horizontalHeaderItem(3)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Precio Unidad", None));
        ___qtablewidgetitem7 = self.Tabla_basedatos.horizontalHeaderItem(4)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Total", None));
        self.Boton_ActualizarBase.setText(QCoreApplication.translate("MainWindow", u"Refrescar", None))
    # retranslateUi

