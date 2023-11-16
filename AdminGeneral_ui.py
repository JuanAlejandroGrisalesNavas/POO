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
from PySide6.QtWidgets import (QApplication, QDateTimeEdit, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1513, 847)
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
"background-color: rgb(255,255,255);\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: #000000ff;\n"
"border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(101, 101, 101);\n"
"border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(155,155,155);\n"
"border-radius: 20px;\n"
"color:  rgb(230,230,230);\n"
"font: 75 15pt \"Yu Gothic UI Semibold\";\n"
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

        self.horizontalSpace_FrameSup = QSpacerItem(943, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpace_FrameSup)

        self.Reloj = QDateTimeEdit(self.frame_superior)
        self.Reloj.setObjectName(u"Reloj")
        self.Reloj.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.Reloj)

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
        self.frame_inferior.setStyleSheet(u"")
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
"	background-color: rgb(101, 101, 101);\n"
"	border-radius: 20px;\n"
"	color: rgb(230,230,230);\n"
"	font: 75 15pt \"Yu Gothic UI Semibold\";\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(155,155,155);\n"
"border-radius: 20px;\n"
"color:  rgb(230,230,230);\n"
"font: 75 15pt \"Yu Gothic UI Semibold\";\n"
"}\n"
"\n"
"")
        self.frame_control.setFrameShape(QFrame.StyledPanel)
        self.frame_control.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_control)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.Boton_usuarios = QPushButton(self.frame_control)
        self.Boton_usuarios.setObjectName(u"Boton_usuarios")
        self.Boton_usuarios.setMinimumSize(QSize(0, 80))
        self.Boton_usuarios.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.Boton_usuarios)

        self.Boton_locales = QPushButton(self.frame_control)
        self.Boton_locales.setObjectName(u"Boton_locales")
        self.Boton_locales.setMinimumSize(QSize(0, 80))
        self.Boton_locales.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.Boton_locales)

        self.Boton_resumenVentas = QPushButton(self.frame_control)
        self.Boton_resumenVentas.setObjectName(u"Boton_resumenVentas")
        self.Boton_resumenVentas.setMinimumSize(QSize(0, 80))
        self.Boton_resumenVentas.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.Boton_resumenVentas)

        self.Boton_pedidos = QPushButton(self.frame_control)
        self.Boton_pedidos.setObjectName(u"Boton_pedidos")
        self.Boton_pedidos.setMinimumSize(QSize(0, 80))
        self.Boton_pedidos.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.Boton_pedidos)

        self.Boton_productos = QPushButton(self.frame_control)
        self.Boton_productos.setObjectName(u"Boton_productos")
        self.Boton_productos.setMinimumSize(QSize(0, 80))
        self.Boton_productos.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.Boton_productos)

        self.Boton_cerrarAbrirDia = QPushButton(self.frame_control)
        self.Boton_cerrarAbrirDia.setObjectName(u"Boton_cerrarAbrirDia")
        self.Boton_cerrarAbrirDia.setMinimumSize(QSize(0, 80))
        self.Boton_cerrarAbrirDia.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.Boton_cerrarAbrirDia)

        self.Boton_cerrarSesion = QPushButton(self.frame_control)
        self.Boton_cerrarSesion.setObjectName(u"Boton_cerrarSesion")
        self.Boton_cerrarSesion.setMinimumSize(QSize(0, 80))
        self.Boton_cerrarSesion.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.Boton_cerrarSesion)


        self.horizontalLayout_2.addWidget(self.frame_control)

        self.frame_contenido = QFrame(self.frame_inferior)
        self.frame_contenido.setObjectName(u"frame_contenido")
        self.frame_contenido.setStyleSheet(u"QFrame{\n"
"background-color: rgb(101, 101, 101);\n"
"}\n"
"\n"
"QLabel{\n"
"font: 75 15pt \"Yu Gothic UI Semibold\";\n"
"background-color: #000000ff;\n"
"color:rgb(255,255,255);\n"
"border:0px solid#14C8DC;\n"
"}\n"
"\n"
"QLineEdit{\n"
"border:0px;\n"
"color: rgb(10,10,10);\n"
"border-bottom:2px solid rgb(255,255,255);\n"
"font: 75 15pt \"Yu Gothic UI Semibold\";\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(201, 201, 201);\n"
"border-radius: 15px;\n"
"color:  rgb(10,10,10);\n"
"font: 75 15pt \"Yu Gothic UI Semibold\";\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(155,155,155);\n"
"border-radius: 15px;\n"
"color:  rgb(230,230,230);\n"
"font: 75 15pt \"Yu Gothic UI Semibold\";\n"
"}\n"
"\n"
"QTableWidget{\n"
"background-color: rgb(255,255,255);\n"
"color:  rgb(230,230,230);\n"
"grindline-color: rgb(255,255,255);\n"
"font-size: 12pt;\n"
"color: #000000;\n"
"}\n"
"\n"
"QHeaderView::section{\n"
"background-color: rgb(255,255,255);\n"
"border:1px solid rgb(10,10,10);\n"
"font-size: 12pt;\n"
""
                        "}\n"
"\n"
"QTableWindget QTableCornerButtom::section{\n"
"background-color: rgb(205,205,205);\n"
"color:  rgb(255,255,255);\n"
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
        self.stacked_PaginaUsuario = QStackedWidget(self.pagina_usuarios)
        self.stacked_PaginaUsuario.setObjectName(u"stacked_PaginaUsuario")
        self.stacked_PaginaUsuario.setGeometry(QRect(10, 110, 1161, 611))
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

        self.Layout_AgregarUsuario = QHBoxLayout()
        self.Layout_AgregarUsuario.setObjectName(u"Layout_AgregarUsuario")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(30)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.Label_NombreUsuario = QLabel(self.Pagina_AgregarUsuario)
        self.Label_NombreUsuario.setObjectName(u"Label_NombreUsuario")

        self.verticalLayout_7.addWidget(self.Label_NombreUsuario)

        self.Label_FuncionUsuario = QLabel(self.Pagina_AgregarUsuario)
        self.Label_FuncionUsuario.setObjectName(u"Label_FuncionUsuario")

        self.verticalLayout_7.addWidget(self.Label_FuncionUsuario)

        self.Label_ContrasenaUsuario = QLabel(self.Pagina_AgregarUsuario)
        self.Label_ContrasenaUsuario.setObjectName(u"Label_ContrasenaUsuario")

        self.verticalLayout_7.addWidget(self.Label_ContrasenaUsuario)

        self.Label_CodigoUsuario = QLabel(self.Pagina_AgregarUsuario)
        self.Label_CodigoUsuario.setObjectName(u"Label_CodigoUsuario")

        self.verticalLayout_7.addWidget(self.Label_CodigoUsuario)


        self.Layout_AgregarUsuario.addLayout(self.verticalLayout_7)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(30)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.lineEdit_NombreUsuario = QLineEdit(self.Pagina_AgregarUsuario)
        self.lineEdit_NombreUsuario.setObjectName(u"lineEdit_NombreUsuario")

        self.verticalLayout_6.addWidget(self.lineEdit_NombreUsuario)

        self.lineEdit_FuncionUsuario = QLineEdit(self.Pagina_AgregarUsuario)
        self.lineEdit_FuncionUsuario.setObjectName(u"lineEdit_FuncionUsuario")

        self.verticalLayout_6.addWidget(self.lineEdit_FuncionUsuario)

        self.lineEdit_ContrasenaUsuario = QLineEdit(self.Pagina_AgregarUsuario)
        self.lineEdit_ContrasenaUsuario.setObjectName(u"lineEdit_ContrasenaUsuario")

        self.verticalLayout_6.addWidget(self.lineEdit_ContrasenaUsuario)

        self.lineEdit_CodigoUsuario = QLineEdit(self.Pagina_AgregarUsuario)
        self.lineEdit_CodigoUsuario.setObjectName(u"lineEdit_CodigoUsuario")

        self.verticalLayout_6.addWidget(self.lineEdit_CodigoUsuario)


        self.Layout_AgregarUsuario.addLayout(self.verticalLayout_6)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.Layout_AgregarUsuario.addItem(self.horizontalSpacer_4)


        self.verticalLayout_8.addLayout(self.Layout_AgregarUsuario)

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

        self.Boton_ConfirmarAgregarUsuario = QPushButton(self.Pagina_AgregarUsuario)
        self.Boton_ConfirmarAgregarUsuario.setObjectName(u"Boton_ConfirmarAgregarUsuario")
        self.Boton_ConfirmarAgregarUsuario.setMinimumSize(QSize(90, 30))

        self.horizontalLayout_6.addWidget(self.Boton_ConfirmarAgregarUsuario)


        self.verticalLayout_8.addLayout(self.horizontalLayout_6)

        self.stacked_PaginaUsuario.addWidget(self.Pagina_AgregarUsuario)
        self.Pagina_EliminarUsuario = QWidget()
        self.Pagina_EliminarUsuario.setObjectName(u"Pagina_EliminarUsuario")
        self.verticalLayout_12 = QVBoxLayout(self.Pagina_EliminarUsuario)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_EliminarUsuario = QLabel(self.Pagina_EliminarUsuario)
        self.label_EliminarUsuario.setObjectName(u"label_EliminarUsuario")
        self.label_EliminarUsuario.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_EliminarUsuario)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.Label_NombreEliminarUsuario = QLabel(self.Pagina_EliminarUsuario)
        self.Label_NombreEliminarUsuario.setObjectName(u"Label_NombreEliminarUsuario")

        self.horizontalLayout_10.addWidget(self.Label_NombreEliminarUsuario)

        self.lineEdit_EliminarUsuario = QLineEdit(self.Pagina_EliminarUsuario)
        self.lineEdit_EliminarUsuario.setObjectName(u"lineEdit_EliminarUsuario")

        self.horizontalLayout_10.addWidget(self.lineEdit_EliminarUsuario)

        self.Boton_BuscarUsuario_2 = QPushButton(self.Pagina_EliminarUsuario)
        self.Boton_BuscarUsuario_2.setObjectName(u"Boton_BuscarUsuario_2")
        self.Boton_BuscarUsuario_2.setMinimumSize(QSize(90, 35))

        self.horizontalLayout_10.addWidget(self.Boton_BuscarUsuario_2)


        self.verticalLayout_12.addLayout(self.horizontalLayout_10)

        self.tabla_eliminarUsuario = QTableWidget(self.Pagina_EliminarUsuario)
        if (self.tabla_eliminarUsuario.columnCount() < 4):
            self.tabla_eliminarUsuario.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabla_eliminarUsuario.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabla_eliminarUsuario.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabla_eliminarUsuario.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tabla_eliminarUsuario.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tabla_eliminarUsuario.setObjectName(u"tabla_eliminarUsuario")

        self.verticalLayout_12.addWidget(self.tabla_eliminarUsuario)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_18 = QLabel(self.Pagina_EliminarUsuario)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(200, 30))

        self.horizontalLayout_11.addWidget(self.label_18)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_7)

        self.Boton_EliminarUsuario_3 = QPushButton(self.Pagina_EliminarUsuario)
        self.Boton_EliminarUsuario_3.setObjectName(u"Boton_EliminarUsuario_3")
        self.Boton_EliminarUsuario_3.setMinimumSize(QSize(120, 30))

        self.horizontalLayout_11.addWidget(self.Boton_EliminarUsuario_3)


        self.verticalLayout_12.addLayout(self.horizontalLayout_11)

        self.stacked_PaginaUsuario.addWidget(self.Pagina_EliminarUsuario)
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
        self.label_BuscarUsuario = QLabel(self.Pagina_ModificarUsuario)
        self.label_BuscarUsuario.setObjectName(u"label_BuscarUsuario")

        self.horizontalLayout_9.addWidget(self.label_BuscarUsuario)

        self.lineEdit_BuscarUsuario = QLineEdit(self.Pagina_ModificarUsuario)
        self.lineEdit_BuscarUsuario.setObjectName(u"lineEdit_BuscarUsuario")

        self.horizontalLayout_9.addWidget(self.lineEdit_BuscarUsuario)

        self.Boton_BuscarUsuario = QPushButton(self.Pagina_ModificarUsuario)
        self.Boton_BuscarUsuario.setObjectName(u"Boton_BuscarUsuario")
        self.Boton_BuscarUsuario.setMinimumSize(QSize(90, 35))

        self.horizontalLayout_9.addWidget(self.Boton_BuscarUsuario)


        self.verticalLayout_11.addLayout(self.horizontalLayout_9)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_4)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_CodigoUsuario = QLabel(self.Pagina_ModificarUsuario)
        self.label_CodigoUsuario.setObjectName(u"label_CodigoUsuario")

        self.verticalLayout_10.addWidget(self.label_CodigoUsuario)

        self.label_NombreUsuario = QLabel(self.Pagina_ModificarUsuario)
        self.label_NombreUsuario.setObjectName(u"label_NombreUsuario")

        self.verticalLayout_10.addWidget(self.label_NombreUsuario)

        self.label_Funcionusuario = QLabel(self.Pagina_ModificarUsuario)
        self.label_Funcionusuario.setObjectName(u"label_Funcionusuario")

        self.verticalLayout_10.addWidget(self.label_Funcionusuario)

        self.label_ContrasenaUsuario = QLabel(self.Pagina_ModificarUsuario)
        self.label_ContrasenaUsuario.setObjectName(u"label_ContrasenaUsuario")

        self.verticalLayout_10.addWidget(self.label_ContrasenaUsuario)


        self.horizontalLayout_8.addLayout(self.verticalLayout_10)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setSpacing(30)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.lineEdit_6 = QLineEdit(self.Pagina_ModificarUsuario)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.verticalLayout_9.addWidget(self.lineEdit_6)

        self.lineEdit_NombreUsuario_2 = QLineEdit(self.Pagina_ModificarUsuario)
        self.lineEdit_NombreUsuario_2.setObjectName(u"lineEdit_NombreUsuario_2")

        self.verticalLayout_9.addWidget(self.lineEdit_NombreUsuario_2)

        self.lineEdit_FuncionUsuario_2 = QLineEdit(self.Pagina_ModificarUsuario)
        self.lineEdit_FuncionUsuario_2.setObjectName(u"lineEdit_FuncionUsuario_2")

        self.verticalLayout_9.addWidget(self.lineEdit_FuncionUsuario_2)

        self.lineEdit_ContrasenaUsuario_2 = QLineEdit(self.Pagina_ModificarUsuario)
        self.lineEdit_ContrasenaUsuario_2.setObjectName(u"lineEdit_ContrasenaUsuario_2")

        self.verticalLayout_9.addWidget(self.lineEdit_ContrasenaUsuario_2)


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

        self.label_3 = QLabel(self.Pagina_ModificarUsuario)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_7.addWidget(self.label_3)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_5)

        self.Boton_AceptarModificarUsuario = QPushButton(self.Pagina_ModificarUsuario)
        self.Boton_AceptarModificarUsuario.setObjectName(u"Boton_AceptarModificarUsuario")
        self.Boton_AceptarModificarUsuario.setMinimumSize(QSize(90, 30))

        self.horizontalLayout_7.addWidget(self.Boton_AceptarModificarUsuario)


        self.verticalLayout_11.addLayout(self.horizontalLayout_7)

        self.stacked_PaginaUsuario.addWidget(self.Pagina_ModificarUsuario)
        self.layoutWidget = QWidget(self.pagina_usuarios)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(310, 10, 511, 98))
        self.Layout_UsuariosCRUD = QHBoxLayout(self.layoutWidget)
        self.Layout_UsuariosCRUD.setSpacing(19)
        self.Layout_UsuariosCRUD.setObjectName(u"Layout_UsuariosCRUD")
        self.Layout_UsuariosCRUD.setContentsMargins(9, 9, 9, 9)
        self.Boton_AgregarUsuario = QPushButton(self.layoutWidget)
        self.Boton_AgregarUsuario.setObjectName(u"Boton_AgregarUsuario")
        self.Boton_AgregarUsuario.setMinimumSize(QSize(80, 40))

        self.Layout_UsuariosCRUD.addWidget(self.Boton_AgregarUsuario)

        self.Boton_ModificaUsuario = QPushButton(self.layoutWidget)
        self.Boton_ModificaUsuario.setObjectName(u"Boton_ModificaUsuario")
        self.Boton_ModificaUsuario.setMinimumSize(QSize(80, 40))

        self.Layout_UsuariosCRUD.addWidget(self.Boton_ModificaUsuario)

        self.Boton_EliminarUsuario = QPushButton(self.layoutWidget)
        self.Boton_EliminarUsuario.setObjectName(u"Boton_EliminarUsuario")
        self.Boton_EliminarUsuario.setMinimumSize(QSize(80, 40))
        self.Boton_EliminarUsuario.setMaximumSize(QSize(300, 16777215))

        self.Layout_UsuariosCRUD.addWidget(self.Boton_EliminarUsuario)

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
        self.Boton_ActualizarBase.setMinimumSize(QSize(100, 40))

        self.horizontalLayout_3.addWidget(self.Boton_ActualizarBase)


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.stacked_Menu.addWidget(self.pagina_ResumenV)
        self.pagina_Pedidos = QWidget()
        self.pagina_Pedidos.setObjectName(u"pagina_Pedidos")
        self.stacked_Menu.addWidget(self.pagina_Pedidos)
        self.pagina_Productos = QWidget()
        self.pagina_Productos.setObjectName(u"pagina_Productos")
        self.layoutWidget_3 = QWidget(self.pagina_Productos)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(300, 10, 511, 98))
        self.Layout_ProductosCRUD = QHBoxLayout(self.layoutWidget_3)
        self.Layout_ProductosCRUD.setSpacing(19)
        self.Layout_ProductosCRUD.setObjectName(u"Layout_ProductosCRUD")
        self.Layout_ProductosCRUD.setContentsMargins(9, 9, 9, 9)
        self.Boton_AgregarProducto = QPushButton(self.layoutWidget_3)
        self.Boton_AgregarProducto.setObjectName(u"Boton_AgregarProducto")
        self.Boton_AgregarProducto.setMinimumSize(QSize(80, 40))

        self.Layout_ProductosCRUD.addWidget(self.Boton_AgregarProducto)

        self.Boton_ModificarProducto = QPushButton(self.layoutWidget_3)
        self.Boton_ModificarProducto.setObjectName(u"Boton_ModificarProducto")
        self.Boton_ModificarProducto.setMinimumSize(QSize(80, 40))

        self.Layout_ProductosCRUD.addWidget(self.Boton_ModificarProducto)

        self.Boton_EliminarProducto = QPushButton(self.layoutWidget_3)
        self.Boton_EliminarProducto.setObjectName(u"Boton_EliminarProducto")
        self.Boton_EliminarProducto.setMinimumSize(QSize(80, 40))
        self.Boton_EliminarProducto.setMaximumSize(QSize(300, 16777215))

        self.Layout_ProductosCRUD.addWidget(self.Boton_EliminarProducto)

        self.stacked_PaginaProductos = QStackedWidget(self.pagina_Productos)
        self.stacked_PaginaProductos.setObjectName(u"stacked_PaginaProductos")
        self.stacked_PaginaProductos.setGeometry(QRect(30, 120, 1151, 601))
        self.Pagina_AgregarProductos = QWidget()
        self.Pagina_AgregarProductos.setObjectName(u"Pagina_AgregarProductos")
        self.verticalLayout_20 = QVBoxLayout(self.Pagina_AgregarProductos)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label_AgregarProducto = QLabel(self.Pagina_AgregarProductos)
        self.label_AgregarProducto.setObjectName(u"label_AgregarProducto")
        self.label_AgregarProducto.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.label_AgregarProducto)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_20.addItem(self.verticalSpacer_9)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setSpacing(30)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.label_CodigoProducto = QLabel(self.Pagina_AgregarProductos)
        self.label_CodigoProducto.setObjectName(u"label_CodigoProducto")

        self.verticalLayout_21.addWidget(self.label_CodigoProducto)

        self.label_NombreProducto = QLabel(self.Pagina_AgregarProductos)
        self.label_NombreProducto.setObjectName(u"label_NombreProducto")

        self.verticalLayout_21.addWidget(self.label_NombreProducto)

        self.label_LocalPertenece = QLabel(self.Pagina_AgregarProductos)
        self.label_LocalPertenece.setObjectName(u"label_LocalPertenece")

        self.verticalLayout_21.addWidget(self.label_LocalPertenece)


        self.horizontalLayout_20.addLayout(self.verticalLayout_21)

        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setSpacing(30)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.lineEdit_CodigoProducto = QLineEdit(self.Pagina_AgregarProductos)
        self.lineEdit_CodigoProducto.setObjectName(u"lineEdit_CodigoProducto")

        self.verticalLayout_22.addWidget(self.lineEdit_CodigoProducto)

        self.lineEdit_NombreProducto = QLineEdit(self.Pagina_AgregarProductos)
        self.lineEdit_NombreProducto.setObjectName(u"lineEdit_NombreProducto")

        self.verticalLayout_22.addWidget(self.lineEdit_NombreProducto)

        self.lineEdit_LocalPertenece = QLineEdit(self.Pagina_AgregarProductos)
        self.lineEdit_LocalPertenece.setObjectName(u"lineEdit_LocalPertenece")

        self.verticalLayout_22.addWidget(self.lineEdit_LocalPertenece)


        self.horizontalLayout_20.addLayout(self.verticalLayout_22)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_13)


        self.verticalLayout_20.addLayout(self.horizontalLayout_20)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_20.addItem(self.verticalSpacer_10)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_26 = QLabel(self.Pagina_AgregarProductos)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMinimumSize(QSize(200, 0))
        self.label_26.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_21.addWidget(self.label_26)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_14)

        self.Boton_ComfimarProductos = QPushButton(self.Pagina_AgregarProductos)
        self.Boton_ComfimarProductos.setObjectName(u"Boton_ComfimarProductos")
        self.Boton_ComfimarProductos.setMinimumSize(QSize(90, 30))

        self.horizontalLayout_21.addWidget(self.Boton_ComfimarProductos)


        self.verticalLayout_20.addLayout(self.horizontalLayout_21)

        self.stacked_PaginaProductos.addWidget(self.Pagina_AgregarProductos)
        self.Pagina_EliminarProductos = QWidget()
        self.Pagina_EliminarProductos.setObjectName(u"Pagina_EliminarProductos")
        self.verticalLayout_23 = QVBoxLayout(self.Pagina_EliminarProductos)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.label_Eliimar = QLabel(self.Pagina_EliminarProductos)
        self.label_Eliimar.setObjectName(u"label_Eliimar")
        self.label_Eliimar.setAlignment(Qt.AlignCenter)

        self.verticalLayout_23.addWidget(self.label_Eliimar)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_NombreProductoEliminar = QLabel(self.Pagina_EliminarProductos)
        self.label_NombreProductoEliminar.setObjectName(u"label_NombreProductoEliminar")

        self.horizontalLayout_22.addWidget(self.label_NombreProductoEliminar)

        self.lineEdit_BuscarProductoEliminar = QLineEdit(self.Pagina_EliminarProductos)
        self.lineEdit_BuscarProductoEliminar.setObjectName(u"lineEdit_BuscarProductoEliminar")

        self.horizontalLayout_22.addWidget(self.lineEdit_BuscarProductoEliminar)

        self.Boton_BuscarProductoEliminar = QPushButton(self.Pagina_EliminarProductos)
        self.Boton_BuscarProductoEliminar.setObjectName(u"Boton_BuscarProductoEliminar")
        self.Boton_BuscarProductoEliminar.setMinimumSize(QSize(90, 35))

        self.horizontalLayout_22.addWidget(self.Boton_BuscarProductoEliminar)


        self.verticalLayout_23.addLayout(self.horizontalLayout_22)

        self.tabla_EliminarLocal_2 = QTableWidget(self.Pagina_EliminarProductos)
        if (self.tabla_EliminarLocal_2.columnCount() < 4):
            self.tabla_EliminarLocal_2.setColumnCount(4)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tabla_EliminarLocal_2.setHorizontalHeaderItem(0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tabla_EliminarLocal_2.setHorizontalHeaderItem(1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tabla_EliminarLocal_2.setHorizontalHeaderItem(2, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tabla_EliminarLocal_2.setHorizontalHeaderItem(3, __qtablewidgetitem12)
        self.tabla_EliminarLocal_2.setObjectName(u"tabla_EliminarLocal_2")

        self.verticalLayout_23.addWidget(self.tabla_EliminarLocal_2)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_30 = QLabel(self.Pagina_EliminarProductos)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMinimumSize(QSize(200, 30))

        self.horizontalLayout_23.addWidget(self.label_30)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_15)

        self.Boton_EliminarProducto_2 = QPushButton(self.Pagina_EliminarProductos)
        self.Boton_EliminarProducto_2.setObjectName(u"Boton_EliminarProducto_2")
        self.Boton_EliminarProducto_2.setMinimumSize(QSize(120, 30))

        self.horizontalLayout_23.addWidget(self.Boton_EliminarProducto_2)


        self.verticalLayout_23.addLayout(self.horizontalLayout_23)

        self.stacked_PaginaProductos.addWidget(self.Pagina_EliminarProductos)
        self.Pagina_ModificarProducto = QWidget()
        self.Pagina_ModificarProducto.setObjectName(u"Pagina_ModificarProducto")
        self.verticalLayout_24 = QVBoxLayout(self.Pagina_ModificarProducto)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.label_ModificarProductos = QLabel(self.Pagina_ModificarProducto)
        self.label_ModificarProductos.setObjectName(u"label_ModificarProductos")
        self.label_ModificarProductos.setAlignment(Qt.AlignCenter)

        self.verticalLayout_24.addWidget(self.label_ModificarProductos)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_NombreProductoModificarLocal = QLabel(self.Pagina_ModificarProducto)
        self.label_NombreProductoModificarLocal.setObjectName(u"label_NombreProductoModificarLocal")

        self.horizontalLayout_24.addWidget(self.label_NombreProductoModificarLocal)

        self.lineEdit_BuscarProducto_ModificarLocal = QLineEdit(self.Pagina_ModificarProducto)
        self.lineEdit_BuscarProducto_ModificarLocal.setObjectName(u"lineEdit_BuscarProducto_ModificarLocal")

        self.horizontalLayout_24.addWidget(self.lineEdit_BuscarProducto_ModificarLocal)

        self.Boton_BuscarProductoModificar = QPushButton(self.Pagina_ModificarProducto)
        self.Boton_BuscarProductoModificar.setObjectName(u"Boton_BuscarProductoModificar")
        self.Boton_BuscarProductoModificar.setMinimumSize(QSize(90, 35))

        self.horizontalLayout_24.addWidget(self.Boton_BuscarProductoModificar)


        self.verticalLayout_24.addLayout(self.horizontalLayout_24)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_24.addItem(self.verticalSpacer_11)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.label_CodigoModificarProducto = QLabel(self.Pagina_ModificarProducto)
        self.label_CodigoModificarProducto.setObjectName(u"label_CodigoModificarProducto")

        self.verticalLayout_25.addWidget(self.label_CodigoModificarProducto)

        self.label_NombreModificarProducto = QLabel(self.Pagina_ModificarProducto)
        self.label_NombreModificarProducto.setObjectName(u"label_NombreModificarProducto")

        self.verticalLayout_25.addWidget(self.label_NombreModificarProducto)

        self.label_LocalPerteneceModificarProducto = QLabel(self.Pagina_ModificarProducto)
        self.label_LocalPerteneceModificarProducto.setObjectName(u"label_LocalPerteneceModificarProducto")

        self.verticalLayout_25.addWidget(self.label_LocalPerteneceModificarProducto)


        self.horizontalLayout_25.addLayout(self.verticalLayout_25)

        self.verticalLayout_26 = QVBoxLayout()
        self.verticalLayout_26.setSpacing(30)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.lineEdit_CodigoModificarProducto = QLineEdit(self.Pagina_ModificarProducto)
        self.lineEdit_CodigoModificarProducto.setObjectName(u"lineEdit_CodigoModificarProducto")

        self.verticalLayout_26.addWidget(self.lineEdit_CodigoModificarProducto)

        self.lineEdit_NombreModificarProducto = QLineEdit(self.Pagina_ModificarProducto)
        self.lineEdit_NombreModificarProducto.setObjectName(u"lineEdit_NombreModificarProducto")

        self.verticalLayout_26.addWidget(self.lineEdit_NombreModificarProducto)

        self.lineEdit_LocalPerteneceModificarProducto = QLineEdit(self.Pagina_ModificarProducto)
        self.lineEdit_LocalPerteneceModificarProducto.setObjectName(u"lineEdit_LocalPerteneceModificarProducto")

        self.verticalLayout_26.addWidget(self.lineEdit_LocalPerteneceModificarProducto)


        self.horizontalLayout_25.addLayout(self.verticalLayout_26)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_16)


        self.verticalLayout_24.addLayout(self.horizontalLayout_25)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_24.addItem(self.verticalSpacer_12)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_36 = QLabel(self.Pagina_ModificarProducto)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setMinimumSize(QSize(0, 50))

        self.horizontalLayout_26.addWidget(self.label_36)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_17)

        self.Boton_ComfirmarModificarProducto_2 = QPushButton(self.Pagina_ModificarProducto)
        self.Boton_ComfirmarModificarProducto_2.setObjectName(u"Boton_ComfirmarModificarProducto_2")
        self.Boton_ComfirmarModificarProducto_2.setMinimumSize(QSize(90, 30))

        self.horizontalLayout_26.addWidget(self.Boton_ComfirmarModificarProducto_2)


        self.verticalLayout_24.addLayout(self.horizontalLayout_26)

        self.stacked_PaginaProductos.addWidget(self.Pagina_ModificarProducto)
        self.stacked_Menu.addWidget(self.pagina_Productos)
        self.pagina_CerrarSesion = QWidget()
        self.pagina_CerrarSesion.setObjectName(u"pagina_CerrarSesion")
        self.Boton_CerrarSesion = QPushButton(self.pagina_CerrarSesion)
        self.Boton_CerrarSesion.setObjectName(u"Boton_CerrarSesion")
        self.Boton_CerrarSesion.setGeometry(QRect(230, 200, 601, 221))
        self.Boton_CerrarSesion.setStyleSheet(u"")
        self.Boton_ComfirmarCerrarSesion = QPushButton(self.pagina_CerrarSesion)
        self.Boton_ComfirmarCerrarSesion.setObjectName(u"Boton_ComfirmarCerrarSesion")
        self.Boton_ComfirmarCerrarSesion.setGeometry(QRect(450, 510, 181, 31))
        self.stacked_Menu.addWidget(self.pagina_CerrarSesion)
        self.pagina_AbrirCerrarDia_2 = QWidget()
        self.pagina_AbrirCerrarDia_2.setObjectName(u"pagina_AbrirCerrarDia_2")
        self.Boton_AbrirDia = QPushButton(self.pagina_AbrirCerrarDia_2)
        self.Boton_AbrirDia.setObjectName(u"Boton_AbrirDia")
        self.Boton_AbrirDia.setGeometry(QRect(140, 210, 341, 251))
        self.Boton_CerrarDia = QPushButton(self.pagina_AbrirCerrarDia_2)
        self.Boton_CerrarDia.setObjectName(u"Boton_CerrarDia")
        self.Boton_CerrarDia.setGeometry(QRect(650, 210, 341, 251))
        self.Boton_ComfirmarCerrarAbrirDia = QPushButton(self.pagina_AbrirCerrarDia_2)
        self.Boton_ComfirmarCerrarAbrirDia.setObjectName(u"Boton_ComfirmarCerrarAbrirDia")
        self.Boton_ComfirmarCerrarAbrirDia.setGeometry(QRect(470, 560, 201, 41))
        self.stacked_Menu.addWidget(self.pagina_AbrirCerrarDia_2)
        self.pagina_locales = QWidget()
        self.pagina_locales.setObjectName(u"pagina_locales")
        self.stacked_PaginaLocal = QStackedWidget(self.pagina_locales)
        self.stacked_PaginaLocal.setObjectName(u"stacked_PaginaLocal")
        self.stacked_PaginaLocal.setGeometry(QRect(20, 110, 1151, 601))
        self.Pagina_AgregarLocal = QWidget()
        self.Pagina_AgregarLocal.setObjectName(u"Pagina_AgregarLocal")
        self.verticalLayout_13 = QVBoxLayout(self.Pagina_AgregarLocal)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_AgregaLocal = QLabel(self.Pagina_AgregarLocal)
        self.label_AgregaLocal.setObjectName(u"label_AgregaLocal")
        self.label_AgregaLocal.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_AgregaLocal)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_5)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setSpacing(30)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_CodigoLocal = QLabel(self.Pagina_AgregarLocal)
        self.label_CodigoLocal.setObjectName(u"label_CodigoLocal")

        self.verticalLayout_14.addWidget(self.label_CodigoLocal)

        self.label_NombreLocal_2 = QLabel(self.Pagina_AgregarLocal)
        self.label_NombreLocal_2.setObjectName(u"label_NombreLocal_2")

        self.verticalLayout_14.addWidget(self.label_NombreLocal_2)

        self.label_TipoComida = QLabel(self.Pagina_AgregarLocal)
        self.label_TipoComida.setObjectName(u"label_TipoComida")

        self.verticalLayout_14.addWidget(self.label_TipoComida)


        self.horizontalLayout_12.addLayout(self.verticalLayout_14)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setSpacing(30)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.lineEdit_CodigoLocal = QLineEdit(self.Pagina_AgregarLocal)
        self.lineEdit_CodigoLocal.setObjectName(u"lineEdit_CodigoLocal")

        self.verticalLayout_15.addWidget(self.lineEdit_CodigoLocal)

        self.lineEdit_NombreLocal = QLineEdit(self.Pagina_AgregarLocal)
        self.lineEdit_NombreLocal.setObjectName(u"lineEdit_NombreLocal")

        self.verticalLayout_15.addWidget(self.lineEdit_NombreLocal)

        self.lineEdit_TipoComida = QLineEdit(self.Pagina_AgregarLocal)
        self.lineEdit_TipoComida.setObjectName(u"lineEdit_TipoComida")

        self.verticalLayout_15.addWidget(self.lineEdit_TipoComida)


        self.horizontalLayout_12.addLayout(self.verticalLayout_15)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_8)


        self.verticalLayout_13.addLayout(self.horizontalLayout_12)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_6)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_24 = QLabel(self.Pagina_AgregarLocal)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMinimumSize(QSize(200, 0))
        self.label_24.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.label_24)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_9)

        self.Boton_ComfimarLocal = QPushButton(self.Pagina_AgregarLocal)
        self.Boton_ComfimarLocal.setObjectName(u"Boton_ComfimarLocal")
        self.Boton_ComfimarLocal.setMinimumSize(QSize(110, 30))

        self.horizontalLayout_13.addWidget(self.Boton_ComfimarLocal)


        self.verticalLayout_13.addLayout(self.horizontalLayout_13)

        self.stacked_PaginaLocal.addWidget(self.Pagina_AgregarLocal)
        self.Pagina_EliminarLocal = QWidget()
        self.Pagina_EliminarLocal.setObjectName(u"Pagina_EliminarLocal")
        self.verticalLayout_16 = QVBoxLayout(self.Pagina_EliminarLocal)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_25 = QLabel(self.Pagina_EliminarLocal)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_25)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_NombreLocal = QLabel(self.Pagina_EliminarLocal)
        self.label_NombreLocal.setObjectName(u"label_NombreLocal")

        self.horizontalLayout_14.addWidget(self.label_NombreLocal)

        self.lineEdit_BuscarLocal = QLineEdit(self.Pagina_EliminarLocal)
        self.lineEdit_BuscarLocal.setObjectName(u"lineEdit_BuscarLocal")

        self.horizontalLayout_14.addWidget(self.lineEdit_BuscarLocal)

        self.Boton_BuscarLocal = QPushButton(self.Pagina_EliminarLocal)
        self.Boton_BuscarLocal.setObjectName(u"Boton_BuscarLocal")
        self.Boton_BuscarLocal.setMinimumSize(QSize(90, 30))

        self.horizontalLayout_14.addWidget(self.Boton_BuscarLocal)


        self.verticalLayout_16.addLayout(self.horizontalLayout_14)

        self.tabla_EliminarLocal = QTableWidget(self.Pagina_EliminarLocal)
        if (self.tabla_EliminarLocal.columnCount() < 4):
            self.tabla_EliminarLocal.setColumnCount(4)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tabla_EliminarLocal.setHorizontalHeaderItem(0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tabla_EliminarLocal.setHorizontalHeaderItem(1, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tabla_EliminarLocal.setHorizontalHeaderItem(2, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tabla_EliminarLocal.setHorizontalHeaderItem(3, __qtablewidgetitem16)
        self.tabla_EliminarLocal.setObjectName(u"tabla_EliminarLocal")

        self.verticalLayout_16.addWidget(self.tabla_EliminarLocal)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_27 = QLabel(self.Pagina_EliminarLocal)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMinimumSize(QSize(200, 30))

        self.horizontalLayout_15.addWidget(self.label_27)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_10)

        self.Boton_EliminarLocal = QPushButton(self.Pagina_EliminarLocal)
        self.Boton_EliminarLocal.setObjectName(u"Boton_EliminarLocal")
        self.Boton_EliminarLocal.setMinimumSize(QSize(120, 30))

        self.horizontalLayout_15.addWidget(self.Boton_EliminarLocal)


        self.verticalLayout_16.addLayout(self.horizontalLayout_15)

        self.stacked_PaginaLocal.addWidget(self.Pagina_EliminarLocal)
        self.Pagina_ModificarLocal = QWidget()
        self.Pagina_ModificarLocal.setObjectName(u"Pagina_ModificarLocal")
        self.verticalLayout_17 = QVBoxLayout(self.Pagina_ModificarLocal)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_28 = QLabel(self.Pagina_ModificarLocal)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.label_28)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_NombreLocalModificarLocal = QLabel(self.Pagina_ModificarLocal)
        self.label_NombreLocalModificarLocal.setObjectName(u"label_NombreLocalModificarLocal")

        self.horizontalLayout_16.addWidget(self.label_NombreLocalModificarLocal)

        self.lineEdit_BuscarLocal_ModificarLocal = QLineEdit(self.Pagina_ModificarLocal)
        self.lineEdit_BuscarLocal_ModificarLocal.setObjectName(u"lineEdit_BuscarLocal_ModificarLocal")

        self.horizontalLayout_16.addWidget(self.lineEdit_BuscarLocal_ModificarLocal)

        self.Boton_BuscarLocal_2 = QPushButton(self.Pagina_ModificarLocal)
        self.Boton_BuscarLocal_2.setObjectName(u"Boton_BuscarLocal_2")
        self.Boton_BuscarLocal_2.setMinimumSize(QSize(90, 30))

        self.horizontalLayout_16.addWidget(self.Boton_BuscarLocal_2)


        self.verticalLayout_17.addLayout(self.horizontalLayout_16)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer_7)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_CodigoModificarLocal = QLabel(self.Pagina_ModificarLocal)
        self.label_CodigoModificarLocal.setObjectName(u"label_CodigoModificarLocal")

        self.verticalLayout_18.addWidget(self.label_CodigoModificarLocal)

        self.label_NombreModificarLocal = QLabel(self.Pagina_ModificarLocal)
        self.label_NombreModificarLocal.setObjectName(u"label_NombreModificarLocal")

        self.verticalLayout_18.addWidget(self.label_NombreModificarLocal)

        self.label_TipoComidaModificarLocal = QLabel(self.Pagina_ModificarLocal)
        self.label_TipoComidaModificarLocal.setObjectName(u"label_TipoComidaModificarLocal")

        self.verticalLayout_18.addWidget(self.label_TipoComidaModificarLocal)


        self.horizontalLayout_17.addLayout(self.verticalLayout_18)

        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setSpacing(30)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.lineEdit_CodigoModificarLocal = QLineEdit(self.Pagina_ModificarLocal)
        self.lineEdit_CodigoModificarLocal.setObjectName(u"lineEdit_CodigoModificarLocal")

        self.verticalLayout_19.addWidget(self.lineEdit_CodigoModificarLocal)

        self.lineEdit_NombreModificarLocal = QLineEdit(self.Pagina_ModificarLocal)
        self.lineEdit_NombreModificarLocal.setObjectName(u"lineEdit_NombreModificarLocal")

        self.verticalLayout_19.addWidget(self.lineEdit_NombreModificarLocal)

        self.lineEdit_20 = QLineEdit(self.Pagina_ModificarLocal)
        self.lineEdit_20.setObjectName(u"lineEdit_20")

        self.verticalLayout_19.addWidget(self.lineEdit_20)


        self.horizontalLayout_17.addLayout(self.verticalLayout_19)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_11)


        self.verticalLayout_17.addLayout(self.horizontalLayout_17)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer_8)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_35 = QLabel(self.Pagina_ModificarLocal)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMinimumSize(QSize(0, 50))

        self.horizontalLayout_18.addWidget(self.label_35)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_12)

        self.Boton_ComfirmarModificarLocal = QPushButton(self.Pagina_ModificarLocal)
        self.Boton_ComfirmarModificarLocal.setObjectName(u"Boton_ComfirmarModificarLocal")
        self.Boton_ComfirmarModificarLocal.setMinimumSize(QSize(90, 30))

        self.horizontalLayout_18.addWidget(self.Boton_ComfirmarModificarLocal)


        self.verticalLayout_17.addLayout(self.horizontalLayout_18)

        self.stacked_PaginaLocal.addWidget(self.Pagina_ModificarLocal)
        self.layoutWidget_2 = QWidget(self.pagina_locales)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(300, 10, 511, 98))
        self.horizontalLayout_19 = QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_19.setSpacing(19)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(9, 9, 9, 9)
        self.Boton_AgregarLocal = QPushButton(self.layoutWidget_2)
        self.Boton_AgregarLocal.setObjectName(u"Boton_AgregarLocal")
        self.Boton_AgregarLocal.setMinimumSize(QSize(80, 40))

        self.horizontalLayout_19.addWidget(self.Boton_AgregarLocal)

        self.Boton_ModificarLocal = QPushButton(self.layoutWidget_2)
        self.Boton_ModificarLocal.setObjectName(u"Boton_ModificarLocal")
        self.Boton_ModificarLocal.setMinimumSize(QSize(80, 40))

        self.horizontalLayout_19.addWidget(self.Boton_ModificarLocal)

        self.Boton_EliminarLocal_2 = QPushButton(self.layoutWidget_2)
        self.Boton_EliminarLocal_2.setObjectName(u"Boton_EliminarLocal_2")
        self.Boton_EliminarLocal_2.setMinimumSize(QSize(80, 40))
        self.Boton_EliminarLocal_2.setMaximumSize(QSize(300, 16777215))

        self.horizontalLayout_19.addWidget(self.Boton_EliminarLocal_2)

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
        self.stacked_PaginaUsuario.setCurrentIndex(2)
        self.stacked_PaginaProductos.setCurrentIndex(1)
        self.stacked_PaginaLocal.setCurrentIndex(1)


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
        self.Boton_productos.setText(QCoreApplication.translate("MainWindow", u"Productos", None))
        self.Boton_cerrarAbrirDia.setText(QCoreApplication.translate("MainWindow", u"Abrir/Cerrar Dia", None))
        self.Boton_cerrarSesion.setText(QCoreApplication.translate("MainWindow", u"Cerrar Sesion", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"AGREGAR USUARIOS", None))
        self.Label_NombreUsuario.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.Label_FuncionUsuario.setText(QCoreApplication.translate("MainWindow", u"Funcion", None))
        self.Label_ContrasenaUsuario.setText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a", None))
        self.Label_CodigoUsuario.setText(QCoreApplication.translate("MainWindow", u"Codigo", None))
        self.label_6.setText("")
        self.Boton_ConfirmarAgregarUsuario.setText(QCoreApplication.translate("MainWindow", u"Aceptar", None))
        self.label_EliminarUsuario.setText(QCoreApplication.translate("MainWindow", u"ELIMINAR USUARIO", None))
        self.Label_NombreEliminarUsuario.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.Boton_BuscarUsuario_2.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        ___qtablewidgetitem = self.tabla_eliminarUsuario.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Nombre", None));
        ___qtablewidgetitem1 = self.tabla_eliminarUsuario.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Producto", None));
        ___qtablewidgetitem2 = self.tabla_eliminarUsuario.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Contrasena", None));
        self.label_18.setText("")
        self.Boton_EliminarUsuario_3.setText(QCoreApplication.translate("MainWindow", u"ELIMINAR", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"MODIFICAR USUARIO", None))
        self.label_BuscarUsuario.setText(QCoreApplication.translate("MainWindow", u"Usuario", None))
        self.Boton_BuscarUsuario.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.label_CodigoUsuario.setText(QCoreApplication.translate("MainWindow", u"Codigo", None))
        self.label_NombreUsuario.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.label_Funcionusuario.setText(QCoreApplication.translate("MainWindow", u"Funcion", None))
        self.label_ContrasenaUsuario.setText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a", None))
        self.label_14.setText("")
        self.label_3.setText("")
        self.Boton_AceptarModificarUsuario.setText(QCoreApplication.translate("MainWindow", u"Aceptar", None))
        self.Boton_AgregarUsuario.setText(QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.Boton_ModificaUsuario.setText(QCoreApplication.translate("MainWindow", u"Modificar", None))
        self.Boton_EliminarUsuario.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"RESUMEN VENTAS", None))
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
        self.Boton_AgregarProducto.setText(QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.Boton_ModificarProducto.setText(QCoreApplication.translate("MainWindow", u"Modificar", None))
        self.Boton_EliminarProducto.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
        self.label_AgregarProducto.setText(QCoreApplication.translate("MainWindow", u"AGREGAR PRODUCTO", None))
        self.label_CodigoProducto.setText(QCoreApplication.translate("MainWindow", u"Codigo", None))
        self.label_NombreProducto.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.label_LocalPertenece.setText(QCoreApplication.translate("MainWindow", u"Local Pertenece", None))
        self.label_26.setText("")
        self.Boton_ComfimarProductos.setText(QCoreApplication.translate("MainWindow", u"Aceptar", None))
        self.label_Eliimar.setText(QCoreApplication.translate("MainWindow", u"ELIMINAR LOCAL", None))
        self.label_NombreProductoEliminar.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.Boton_BuscarProductoEliminar.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        ___qtablewidgetitem8 = self.tabla_EliminarLocal_2.horizontalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Nombre", None));
        ___qtablewidgetitem9 = self.tabla_EliminarLocal_2.horizontalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Producto", None));
        ___qtablewidgetitem10 = self.tabla_EliminarLocal_2.horizontalHeaderItem(2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Contrasena", None));
        self.label_30.setText("")
        self.Boton_EliminarProducto_2.setText(QCoreApplication.translate("MainWindow", u"ELIMINAR", None))
        self.label_ModificarProductos.setText(QCoreApplication.translate("MainWindow", u"MODIFICAR PRODUCTOS", None))
        self.label_NombreProductoModificarLocal.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.Boton_BuscarProductoModificar.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.label_CodigoModificarProducto.setText(QCoreApplication.translate("MainWindow", u"Codigo", None))
        self.label_NombreModificarProducto.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.label_LocalPerteneceModificarProducto.setText(QCoreApplication.translate("MainWindow", u"Tipo Comida", None))
        self.label_36.setText("")
        self.Boton_ComfirmarModificarProducto_2.setText(QCoreApplication.translate("MainWindow", u"Aceptar", None))
        self.Boton_CerrarSesion.setText(QCoreApplication.translate("MainWindow", u"CERRAR SESION", None))
        self.Boton_ComfirmarCerrarSesion.setText(QCoreApplication.translate("MainWindow", u"COMFIRMAR", None))
        self.Boton_AbrirDia.setText(QCoreApplication.translate("MainWindow", u"ABRIR DIA ", None))
        self.Boton_CerrarDia.setText(QCoreApplication.translate("MainWindow", u"CERRAR DIA ", None))
        self.Boton_ComfirmarCerrarAbrirDia.setText(QCoreApplication.translate("MainWindow", u"COMFIRMAR", None))
        self.label_AgregaLocal.setText(QCoreApplication.translate("MainWindow", u"AGREGAR LOCAL", None))
        self.label_CodigoLocal.setText(QCoreApplication.translate("MainWindow", u"Codigo", None))
        self.label_NombreLocal_2.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.label_TipoComida.setText(QCoreApplication.translate("MainWindow", u"Tipo Comida", None))
        self.label_24.setText("")
        self.Boton_ComfimarLocal.setText(QCoreApplication.translate("MainWindow", u"Comfirmar", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"ELIMINAR LOCAL", None))
        self.label_NombreLocal.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.Boton_BuscarLocal.setText(QCoreApplication.translate("MainWindow", u"BUSCAR", None))
        ___qtablewidgetitem11 = self.tabla_EliminarLocal.horizontalHeaderItem(0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Nombre", None));
        ___qtablewidgetitem12 = self.tabla_EliminarLocal.horizontalHeaderItem(1)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Producto", None));
        ___qtablewidgetitem13 = self.tabla_EliminarLocal.horizontalHeaderItem(2)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Contrasena", None));
        self.label_27.setText("")
        self.Boton_EliminarLocal.setText(QCoreApplication.translate("MainWindow", u"ELIMINAR", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"MODIFICAR LOCAL", None))
        self.label_NombreLocalModificarLocal.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.Boton_BuscarLocal_2.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.label_CodigoModificarLocal.setText(QCoreApplication.translate("MainWindow", u"Codigo", None))
        self.label_NombreModificarLocal.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.label_TipoComidaModificarLocal.setText(QCoreApplication.translate("MainWindow", u"Tipo Comida", None))
        self.label_35.setText("")
        self.Boton_ComfirmarModificarLocal.setText(QCoreApplication.translate("MainWindow", u"Aceptar", None))
        self.Boton_AgregarLocal.setText(QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.Boton_ModificarLocal.setText(QCoreApplication.translate("MainWindow", u"Modificar", None))
        self.Boton_EliminarLocal_2.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
    # retranslateUi

