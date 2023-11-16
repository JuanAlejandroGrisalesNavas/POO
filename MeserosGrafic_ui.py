# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MeserosGrafic.ui'
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
from PySide6.QtWidgets import (QApplication, QDateTimeEdit, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLayout,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QTableView, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1583, 842)
        MainWindow.setStyleSheet(u"background-color: rgb(10, 101, 112);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(10, 101, 112);")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 1581, 841))
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
        self.Boton_menu.setMinimumSize(QSize(400, 0))
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
        self.frame_control.setMinimumSize(QSize(400, 0))
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
        self.Boton_Atras = QPushButton(self.frame_control)
        self.Boton_Atras.setObjectName(u"Boton_Atras")
        self.Boton_Atras.setMinimumSize(QSize(40, 70))
        self.Boton_Atras.setStyleSheet(u"\n"
"QPushButton{\n"
"font: 75 15pt \"Yu Gothic UI Semibold\";\n"
"	color: rgb(0,0,0);\n"
"	background-color: rgb(38, 0, 0);\n"
"border-radius: 30px;\n"
"\n"
"}\n"
"QPushButton{\n"
"background-color: rgb(0, 170, 127);\n"
"	color:rgb(0,0,0)\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"	background-color: rgb(179, 179, 179);\n"
"\n"
"}")

        self.verticalLayout_3.addWidget(self.Boton_Atras)

        self.tabla__Pedido = QTableView(self.frame_control)
        self.tabla__Pedido.setObjectName(u"tabla__Pedido")

        self.verticalLayout_3.addWidget(self.tabla__Pedido)

        self.Boton_comfirmarPedido = QPushButton(self.frame_control)
        self.Boton_comfirmarPedido.setObjectName(u"Boton_comfirmarPedido")
        self.Boton_comfirmarPedido.setMinimumSize(QSize(0, 120))
        self.Boton_comfirmarPedido.setStyleSheet(u"\n"
"QPushButton{\n"
"font: 75 15pt \"Yu Gothic UI Semibold\";\n"
"	color: rgb(0,0,0);\n"
"	background-color: rgb(38, 0, 0);\n"
"border-radius: 30px;\n"
"\n"
"}\n"
"QPushButton{\n"
"background-color: rgb(0, 170, 127);\n"
"	color:rgb(0,0,0)\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"	background-color: rgb(179, 179, 179);\n"
"\n"
"}")

        self.verticalLayout_3.addWidget(self.Boton_comfirmarPedido)


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
        self.stacked_controlPaginas = QStackedWidget(self.pagina_usuarios)
        self.stacked_controlPaginas.setObjectName(u"stacked_controlPaginas")
        self.stacked_controlPaginas.setGeometry(QRect(10, 150, 1131, 571))
        self.Pagina_Comida = QWidget()
        self.Pagina_Comida.setObjectName(u"Pagina_Comida")
        self.layoutWidget_2 = QWidget(self.Pagina_Comida)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(10, 20, 731, 531))
        self.gridLayout_3 = QGridLayout(self.layoutWidget_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.Producto_3 = QPushButton(self.layoutWidget_2)
        self.Producto_3.setObjectName(u"Producto_3")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Producto_3.sizePolicy().hasHeightForWidth())
        self.Producto_3.setSizePolicy(sizePolicy)
        self.Producto_3.setStyleSheet(u"QPushButton{\n"
"font: 75 15pt \"Yu Gothic UI Semibold\";\n"
"	color: rgb(0,0,0);\n"
"	background-color: rgb(38, 0, 0);\n"
"border-radius: 30px;\n"
"\n"
"}\n"
"QPushButton{\n"
"background-color: rgb(230,230,230);\n"
"	color:rgb(0,0,0)\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"	background-color: rgb(179, 179, 179);\n"
"\n"
"}")

        self.gridLayout_3.addWidget(self.Producto_3, 0, 3, 1, 1)

        self.Mesa2_4 = QPushButton(self.layoutWidget_2)
        self.Mesa2_4.setObjectName(u"Mesa2_4")
        sizePolicy.setHeightForWidth(self.Mesa2_4.sizePolicy().hasHeightForWidth())
        self.Mesa2_4.setSizePolicy(sizePolicy)
        self.Mesa2_4.setStyleSheet(u"QPushButton{\n"
"font: 75 15pt \"Yu Gothic UI Semibold\";\n"
"	color: rgb(0,0,0);\n"
"	background-color: rgb(38, 0, 0);\n"
"border-radius: 30px;\n"
"\n"
"}\n"
"QPushButton{\n"
"background-color: rgb(230,230,230);\n"
"	color:rgb(0,0,0)\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"	background-color: rgb(179, 179, 179);\n"
"\n"
"}")

        self.gridLayout_3.addWidget(self.Mesa2_4, 0, 1, 1, 1)

        self.Producto_2 = QPushButton(self.layoutWidget_2)
        self.Producto_2.setObjectName(u"Producto_2")
        sizePolicy.setHeightForWidth(self.Producto_2.sizePolicy().hasHeightForWidth())
        self.Producto_2.setSizePolicy(sizePolicy)
        self.Producto_2.setStyleSheet(u"QPushButton{\n"
"font: 75 15pt \"Yu Gothic UI Semibold\";\n"
"	color: rgb(0,0,0);\n"
"	background-color: rgb(38, 0, 0);\n"
"border-radius: 30px;\n"
"\n"
"}\n"
"QPushButton{\n"
"background-color: rgb(230,230,230);\n"
"	color:rgb(0,0,0)\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"	background-color: rgb(179, 179, 179);\n"
"\n"
"}")

        self.gridLayout_3.addWidget(self.Producto_2, 0, 2, 1, 1)

        self.layoutWidget_3 = QWidget(self.Pagina_Comida)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(780, 10, 311, 171))
        self.gridLayout_4 = QGridLayout(self.layoutWidget_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.Boton_ImprimirFactura = QPushButton(self.layoutWidget_3)
        self.Boton_ImprimirFactura.setObjectName(u"Boton_ImprimirFactura")
        sizePolicy.setHeightForWidth(self.Boton_ImprimirFactura.sizePolicy().hasHeightForWidth())
        self.Boton_ImprimirFactura.setSizePolicy(sizePolicy)
        self.Boton_ImprimirFactura.setLayoutDirection(Qt.RightToLeft)
        self.Boton_ImprimirFactura.setStyleSheet(u"QPushButton{\n"
"font: 75 15pt \"Yu Gothic UI Semibold\";\n"
"	color: rgb(0,0,0);\n"
"	background-color: rgb(38, 0, 0);\n"
"border-radius: 30px;\n"
"\n"
"}\n"
"QPushButton{\n"
"background-color: rgb(230,230,230);\n"
"	color:rgb(0,0,0)\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"	background-color: rgb(179, 179, 179);\n"
"\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u"../Imagenes/dinero.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Boton_ImprimirFactura.setIcon(icon5)
        self.Boton_ImprimirFactura.setIconSize(QSize(40, 40))

        self.gridLayout_4.addWidget(self.Boton_ImprimirFactura, 1, 1, 1, 1)

        self.Boton_NotaDelProducto = QPushButton(self.layoutWidget_3)
        self.Boton_NotaDelProducto.setObjectName(u"Boton_NotaDelProducto")
        sizePolicy.setHeightForWidth(self.Boton_NotaDelProducto.sizePolicy().hasHeightForWidth())
        self.Boton_NotaDelProducto.setSizePolicy(sizePolicy)
        self.Boton_NotaDelProducto.setStyleSheet(u"QPushButton{\n"
"font: 75 15pt \"Yu Gothic UI Semibold\";\n"
"	color: rgb(0,0,0);\n"
"	background-color: rgb(38, 0, 0);\n"
"border-radius: 30px;\n"
"\n"
"}\n"
"QPushButton{\n"
"background-color: rgb(230,230,230);\n"
"	color:rgb(0,0,0)\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"	background-color: rgb(179, 179, 179);\n"
"\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u"../Imagenes/notas.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Boton_NotaDelProducto.setIcon(icon6)
        self.Boton_NotaDelProducto.setIconSize(QSize(40, 40))

        self.gridLayout_4.addWidget(self.Boton_NotaDelProducto, 1, 2, 1, 1)

        self.Boton_DescartarPedido = QPushButton(self.layoutWidget_3)
        self.Boton_DescartarPedido.setObjectName(u"Boton_DescartarPedido")
        sizePolicy.setHeightForWidth(self.Boton_DescartarPedido.sizePolicy().hasHeightForWidth())
        self.Boton_DescartarPedido.setSizePolicy(sizePolicy)
        self.Boton_DescartarPedido.setLayoutDirection(Qt.RightToLeft)
        self.Boton_DescartarPedido.setStyleSheet(u"QPushButton{\n"
"font: 75 15pt \"Yu Gothic UI Semibold\";\n"
"	color: rgb(0,0,0);\n"
"	background-color: rgb(38, 0, 0);\n"
"border-radius: 30px;\n"
"\n"
"}\n"
"QPushButton{\n"
"background-color: rgb(230,230,230);\n"
"	color:rgb(0,0,0)\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"	background-color: rgb(179, 179, 179);\n"
"\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u"../Imagenes/descarte.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Boton_DescartarPedido.setIcon(icon7)
        self.Boton_DescartarPedido.setIconSize(QSize(50, 50))

        self.gridLayout_4.addWidget(self.Boton_DescartarPedido, 0, 1, 1, 1)

        self.Boton_Total = QPushButton(self.layoutWidget_3)
        self.Boton_Total.setObjectName(u"Boton_Total")
        sizePolicy.setHeightForWidth(self.Boton_Total.sizePolicy().hasHeightForWidth())
        self.Boton_Total.setSizePolicy(sizePolicy)
        self.Boton_Total.setLayoutDirection(Qt.RightToLeft)
        self.Boton_Total.setStyleSheet(u"QPushButton{\n"
"font: 75 15pt \"Yu Gothic UI Semibold\";\n"
"	color: rgb(0,0,0);\n"
"	background-color: rgb(38, 0, 0);\n"
"border-radius: 30px;\n"
"\n"
"}\n"
"QPushButton{\n"
"background-color: rgb(230,230,230);\n"
"	color:rgb(0,0,0)\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"	background-color: rgb(179, 179, 179);\n"
"\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u"../Imagenes/factura.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Boton_Total.setIcon(icon8)
        self.Boton_Total.setIconSize(QSize(50, 50))

        self.gridLayout_4.addWidget(self.Boton_Total, 0, 2, 1, 1)

        self.Boton_AgregarProducto = QPushButton(self.Pagina_Comida)
        self.Boton_AgregarProducto.setObjectName(u"Boton_AgregarProducto")
        self.Boton_AgregarProducto.setGeometry(QRect(780, 470, 331, 61))
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Boton_AgregarProducto.sizePolicy().hasHeightForWidth())
        self.Boton_AgregarProducto.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setFamilies([u"Yu Gothic UI Semibold"])
        font.setPointSize(15)
        font.setWeight(QFont.)
        font.setItalic(False)
        font.setStrikeOut(False)
        font.setStyleStrategy(QFont.PreferDefault)
        self.Boton_AgregarProducto.setFont(font)
        self.Boton_AgregarProducto.setLayoutDirection(Qt.LeftToRight)
        self.Boton_AgregarProducto.setStyleSheet(u"QPushButton{\n"
"font: 75 15pt \"Yu Gothic UI Semibold\";\n"
"	color: rgb(0,0,0);\n"
"	background-color: rgb(38, 0, 0);\n"
"border-radius: 30px;\n"
"\n"
"}\n"
"QPushButton{\n"
"background-color: rgb(230,230,230);\n"
"	color:rgb(0,0,0)\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"	background-color: rgb(179, 179, 179);\n"
"\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u"../Users/holan/OneDrive/Escritorio/tabla.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Boton_AgregarProducto.setIcon(icon9)
        self.Boton_AgregarProducto.setIconSize(QSize(100, 100))
        self.Boton_Cantidad = QPushButton(self.Pagina_Comida)
        self.Boton_Cantidad.setObjectName(u"Boton_Cantidad")
        self.Boton_Cantidad.setGeometry(QRect(850, 310, 178, 141))
        sizePolicy1.setHeightForWidth(self.Boton_Cantidad.sizePolicy().hasHeightForWidth())
        self.Boton_Cantidad.setSizePolicy(sizePolicy1)
        self.Boton_Cantidad.setFont(font)
        self.Boton_Cantidad.setLayoutDirection(Qt.LeftToRight)
        self.Boton_Cantidad.setStyleSheet(u"QPushButton{\n"
"font: 75 15pt \"Yu Gothic UI Semibold\";\n"
"	color: rgb(0,0,0);\n"
"	background-color: rgb(38, 0, 0);\n"
"border-radius: 30px;\n"
"\n"
"}\n"
"QPushButton{\n"
"background-color: rgb(230,230,230);\n"
"	color:rgb(0,0,0)\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"	background-color: rgb(179, 179, 179);\n"
"\n"
"}")
        self.Boton_Cantidad.setIcon(icon9)
        self.Boton_Cantidad.setIconSize(QSize(100, 100))
        self.Line_Notas = QLineEdit(self.Pagina_Comida)
        self.Line_Notas.setObjectName(u"Line_Notas")
        self.Line_Notas.setGeometry(QRect(780, 210, 311, 91))
        self.stacked_controlPaginas.addWidget(self.Pagina_Comida)
        self.Pagina_Restaurantes = QWidget()
        self.Pagina_Restaurantes.setObjectName(u"Pagina_Restaurantes")
        self.verticalLayout_8 = QVBoxLayout(self.Pagina_Restaurantes)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.Layout_AgregarUsuario = QHBoxLayout()
        self.Layout_AgregarUsuario.setObjectName(u"Layout_AgregarUsuario")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(30)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")

        self.Layout_AgregarUsuario.addLayout(self.verticalLayout_7)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(30)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.Restaurante_3 = QPushButton(self.Pagina_Restaurantes)
        self.Restaurante_3.setObjectName(u"Restaurante_3")
        sizePolicy.setHeightForWidth(self.Restaurante_3.sizePolicy().hasHeightForWidth())
        self.Restaurante_3.setSizePolicy(sizePolicy)
        self.Restaurante_3.setMinimumSize(QSize(300, 200))
        self.Restaurante_3.setStyleSheet(u"QPushButton{\n"
"font: 75 15pt \"Yu Gothic UI Semibold\";\n"
"	color: rgb(0,0,0);\n"
"	background-color: rgb(38, 0, 0);\n"
"border-radius: 30px;\n"
"\n"
"}\n"
"QPushButton{\n"
"background-color: rgb(230,230,230);\n"
"	color:rgb(0,0,0)\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"	background-color: rgb(179, 179, 179);\n"
"\n"
"}")

        self.gridLayout_2.addWidget(self.Restaurante_3, 1, 6, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.Restaurante_2 = QPushButton(self.Pagina_Restaurantes)
        self.Restaurante_2.setObjectName(u"Restaurante_2")
        sizePolicy.setHeightForWidth(self.Restaurante_2.sizePolicy().hasHeightForWidth())
        self.Restaurante_2.setSizePolicy(sizePolicy)
        self.Restaurante_2.setMinimumSize(QSize(300, 200))
        self.Restaurante_2.setStyleSheet(u"QPushButton{\n"
"font: 75 15pt \"Yu Gothic UI Semibold\";\n"
"	color: rgb(0,0,0);\n"
"	background-color: rgb(38, 0, 0);\n"
"border-radius: 30px;\n"
"\n"
"}\n"
"QPushButton{\n"
"background-color: rgb(230,230,230);\n"
"	color:rgb(0,0,0)\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"	background-color: rgb(179, 179, 179);\n"
"\n"
"}")

        self.gridLayout_2.addWidget(self.Restaurante_2, 1, 4, 1, 1)

        self.Restaurante_1 = QPushButton(self.Pagina_Restaurantes)
        self.Restaurante_1.setObjectName(u"Restaurante_1")
        sizePolicy.setHeightForWidth(self.Restaurante_1.sizePolicy().hasHeightForWidth())
        self.Restaurante_1.setSizePolicy(sizePolicy)
        self.Restaurante_1.setMinimumSize(QSize(300, 200))
        self.Restaurante_1.setStyleSheet(u"QPushButton{\n"
"font: 75 15pt \"Yu Gothic UI Semibold\";\n"
"	color: rgb(0,0,0);\n"
"	background-color: rgb(38, 0, 0);\n"
"border-radius: 30px;\n"
"\n"
"}\n"
"QPushButton{\n"
"background-color: rgb(230,230,230);\n"
"	color:rgb(0,0,0)\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"	background-color: rgb(179, 179, 179);\n"
"\n"
"}")

        self.gridLayout_2.addWidget(self.Restaurante_1, 1, 3, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 1, 7, 1, 1)


        self.verticalLayout_6.addLayout(self.gridLayout_2)


        self.Layout_AgregarUsuario.addLayout(self.verticalLayout_6)


        self.verticalLayout_8.addLayout(self.Layout_AgregarUsuario)

        self.stacked_controlPaginas.addWidget(self.Pagina_Restaurantes)
        self.Pagina_Mesas = QWidget()
        self.Pagina_Mesas.setObjectName(u"Pagina_Mesas")
        self.verticalLayout_12 = QVBoxLayout(self.Pagina_Mesas)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.Mesa12 = QPushButton(self.Pagina_Mesas)
        self.Mesa12.setObjectName(u"Mesa12")
        sizePolicy.setHeightForWidth(self.Mesa12.sizePolicy().hasHeightForWidth())
        self.Mesa12.setSizePolicy(sizePolicy)
        self.Mesa12.setStyleSheet(u"QPushButton{\n"
"font: 75 15pt \"Yu Gothic UI Semibold\";\n"
"	color: rgb(0,0,0);\n"
"	background-color: rgb(38, 0, 0);\n"
"border-radius: 30px;\n"
"\n"
"}\n"
"QPushButton{\n"
"background-color: rgb(230,230,230);\n"
"	color:rgb(0,0,0)\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"	background-color: rgb(179, 179, 179);\n"
"\n"
"}")

        self.gridLayout.addWidget(self.Mesa12, 3, 4, 1, 1)

        self.Mesa2 = QPushButton(self.Pagina_Mesas)
        self.Mesa2.setObjectName(u"Mesa2")
        sizePolicy.setHeightForWidth(self.Mesa2.sizePolicy().hasHeightForWidth())
        self.Mesa2.setSizePolicy(sizePolicy)
        self.Mesa2.setStyleSheet(u"QPushButton{\n"
"font: 75 15pt \"Yu Gothic UI Semibold\";\n"
"	color: rgb(0,0,0);\n"
"	background-color: rgb(38, 0, 0);\n"
"border-radius: 30px;\n"
"\n"
"}\n"
"QPushButton{\n"
"background-color: rgb(230,230,230);\n"
"	color:rgb(0,0,0)\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"	background-color: rgb(179, 179, 179);\n"
"\n"
"}")

        self.gridLayout.addWidget(self.Mesa2, 0, 2, 1, 1)

        self.Mesa8 = QPushButton(self.Pagina_Mesas)
        self.Mesa8.setObjectName(u"Mesa8")
        sizePolicy.setHeightForWidth(self.Mesa8.sizePolicy().hasHeightForWidth())
        self.Mesa8.setSizePolicy(sizePolicy)
        self.Mesa8.setStyleSheet(u"QPushButton{\n"
"font: 75 15pt \"Yu Gothic UI Semibold\";\n"
"	color: rgb(0,0,0);\n"
"	background-color: rgb(38, 0, 0);\n"
"border-radius: 30px;\n"
"\n"
"}\n"
"QPushButton{\n"
"background-color: rgb(230,230,230);\n"
"	color:rgb(0,0,0)\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"	background-color: rgb(179, 179, 179);\n"
"\n"
"}")

        self.gridLayout.addWidget(self.Mesa8, 2, 4, 1, 1)

        self.Mesa7 = QPushButton(self.Pagina_Mesas)
        self.Mesa7.setObjectName(u"Mesa7")
        sizePolicy.setHeightForWidth(self.Mesa7.sizePolicy().hasHeightForWidth())
        self.Mesa7.setSizePolicy(sizePolicy)
        self.Mesa7.setStyleSheet(u"QPushButton{\n"
"font: 75 15pt \"Yu Gothic UI Semibold\";\n"
"	color: rgb(0,0,0);\n"
"	background-color: rgb(38, 0, 0);\n"
"border-radius: 30px;\n"
"\n"
"}\n"
"QPushButton{\n"
"background-color: rgb(230,230,230);\n"
"	color:rgb(0,0,0)\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"	background-color: rgb(179, 179, 179);\n"
"\n"
"}")

        self.gridLayout.addWidget(self.Mesa7, 2, 3, 1, 1)

        self.Mesa9 = QPushButton(self.Pagina_Mesas)
        self.Mesa9.setObjectName(u"Mesa9")
        sizePolicy.setHeightForWidth(self.Mesa9.sizePolicy().hasHeightForWidth())
        self.Mesa9.setSizePolicy(sizePolicy)
        self.Mesa9.setStyleSheet(u"QPushButton{\n"
"font: 75 15pt \"Yu Gothic UI Semibold\";\n"
"	color: rgb(0,0,0);\n"
"	background-color: rgb(38, 0, 0);\n"
"border-radius: 30px;\n"
"\n"
"}\n"
"QPushButton{\n"
"background-color: rgb(230,230,230);\n"
"	color:rgb(0,0,0)\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"	background-color: rgb(179, 179, 179);\n"
"\n"
"}")

        self.gridLayout.addWidget(self.Mesa9, 3, 0, 1, 1)

        self.Mesa1 = QPushButton(self.Pagina_Mesas)
        self.Mesa1.setObjectName(u"Mesa1")
        sizePolicy1.setHeightForWidth(self.Mesa1.sizePolicy().hasHeightForWidth())
        self.Mesa1.setSizePolicy(sizePolicy1)
        self.Mesa1.setFont(font)
        self.Mesa1.setLayoutDirection(Qt.LeftToRight)
        self.Mesa1.setStyleSheet(u"QPushButton{\n"
"font: 75 15pt \"Yu Gothic UI Semibold\";\n"
"	color: rgb(0,0,0);\n"
"	background-color: rgb(38, 0, 0);\n"
"border-radius: 30px;\n"
"\n"
"}\n"
"QPushButton{\n"
"background-color: rgb(230,230,230);\n"
"	color:rgb(0,0,0)\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"	background-color: rgb(179, 179, 179);\n"
"\n"
"}")
        self.Mesa1.setIcon(icon9)
        self.Mesa1.setIconSize(QSize(100, 100))

        self.gridLayout.addWidget(self.Mesa1, 0, 0, 1, 1)

        self.Mesa10 = QPushButton(self.Pagina_Mesas)
        self.Mesa10.setObjectName(u"Mesa10")
        sizePolicy.setHeightForWidth(self.Mesa10.sizePolicy().hasHeightForWidth())
        self.Mesa10.setSizePolicy(sizePolicy)
        self.Mesa10.setStyleSheet(u"QPushButton{\n"
"font: 75 15pt \"Yu Gothic UI Semibold\";\n"
"	color: rgb(0,0,0);\n"
"	background-color: rgb(38, 0, 0);\n"
"border-radius: 30px;\n"
"\n"
"}\n"
"QPushButton{\n"
"background-color: rgb(230,230,230);\n"
"	color:rgb(0,0,0)\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"	background-color: rgb(179, 179, 179);\n"
"\n"
"}")

        self.gridLayout.addWidget(self.Mesa10, 3, 2, 1, 1)

        self.Mesa5 = QPushButton(self.Pagina_Mesas)
        self.Mesa5.setObjectName(u"Mesa5")
        sizePolicy.setHeightForWidth(self.Mesa5.sizePolicy().hasHeightForWidth())
        self.Mesa5.setSizePolicy(sizePolicy)
        self.Mesa5.setStyleSheet(u"QPushButton{\n"
"font: 75 15pt \"Yu Gothic UI Semibold\";\n"
"	color: rgb(0,0,0);\n"
"	background-color: rgb(38, 0, 0);\n"
"border-radius: 30px;\n"
"\n"
"}\n"
"QPushButton{\n"
"background-color: rgb(230,230,230);\n"
"	color:rgb(0,0,0)\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"	background-color: rgb(179, 179, 179);\n"
"\n"
"}")

        self.gridLayout.addWidget(self.Mesa5, 2, 0, 1, 1)

        self.Mesa4 = QPushButton(self.Pagina_Mesas)
        self.Mesa4.setObjectName(u"Mesa4")
        sizePolicy.setHeightForWidth(self.Mesa4.sizePolicy().hasHeightForWidth())
        self.Mesa4.setSizePolicy(sizePolicy)
        self.Mesa4.setStyleSheet(u"QPushButton{\n"
"font: 75 15pt \"Yu Gothic UI Semibold\";\n"
"	color: rgb(0,0,0);\n"
"	background-color: rgb(38, 0, 0);\n"
"border-radius: 30px;\n"
"\n"
"}\n"
"QPushButton{\n"
"background-color: rgb(230,230,230);\n"
"	color:rgb(0,0,0)\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"	background-color: rgb(179, 179, 179);\n"
"\n"
"}")

        self.gridLayout.addWidget(self.Mesa4, 0, 4, 1, 1)

        self.Mesa11 = QPushButton(self.Pagina_Mesas)
        self.Mesa11.setObjectName(u"Mesa11")
        sizePolicy.setHeightForWidth(self.Mesa11.sizePolicy().hasHeightForWidth())
        self.Mesa11.setSizePolicy(sizePolicy)
        self.Mesa11.setStyleSheet(u"QPushButton{\n"
"font: 75 15pt \"Yu Gothic UI Semibold\";\n"
"	color: rgb(0,0,0);\n"
"	background-color: rgb(38, 0, 0);\n"
"border-radius: 30px;\n"
"\n"
"}\n"
"QPushButton{\n"
"background-color: rgb(230,230,230);\n"
"	color:rgb(0,0,0)\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"	background-color: rgb(179, 179, 179);\n"
"\n"
"}")

        self.gridLayout.addWidget(self.Mesa11, 3, 3, 1, 1)

        self.Mesa3 = QPushButton(self.Pagina_Mesas)
        self.Mesa3.setObjectName(u"Mesa3")
        sizePolicy.setHeightForWidth(self.Mesa3.sizePolicy().hasHeightForWidth())
        self.Mesa3.setSizePolicy(sizePolicy)
        self.Mesa3.setStyleSheet(u"QPushButton{\n"
"font: 75 15pt \"Yu Gothic UI Semibold\";\n"
"	color: rgb(0,0,0);\n"
"	background-color: rgb(38, 0, 0);\n"
"border-radius: 30px;\n"
"\n"
"}\n"
"QPushButton{\n"
"background-color: rgb(230,230,230);\n"
"	color:rgb(0,0,0)\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"	background-color: rgb(179, 179, 179);\n"
"\n"
"}")

        self.gridLayout.addWidget(self.Mesa3, 0, 3, 1, 1)

        self.Mesa6 = QPushButton(self.Pagina_Mesas)
        self.Mesa6.setObjectName(u"Mesa6")
        sizePolicy.setHeightForWidth(self.Mesa6.sizePolicy().hasHeightForWidth())
        self.Mesa6.setSizePolicy(sizePolicy)
        self.Mesa6.setStyleSheet(u"QPushButton{\n"
"font: 75 15pt \"Yu Gothic UI Semibold\";\n"
"	color: rgb(0,0,0);\n"
"	background-color: rgb(38, 0, 0);\n"
"border-radius: 30px;\n"
"\n"
"}\n"
"QPushButton{\n"
"background-color: rgb(230,230,230);\n"
"	color:rgb(0,0,0)\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"	background-color: rgb(179, 179, 179);\n"
"\n"
"}")

        self.gridLayout.addWidget(self.Mesa6, 2, 2, 1, 1)


        self.horizontalLayout_10.addLayout(self.gridLayout)


        self.verticalLayout_12.addLayout(self.horizontalLayout_10)

        self.stacked_controlPaginas.addWidget(self.Pagina_Mesas)
        self.Pagina_SeleccionMesero = QWidget()
        self.Pagina_SeleccionMesero.setObjectName(u"Pagina_SeleccionMesero")
        self.verticalLayout_11 = QVBoxLayout(self.Pagina_SeleccionMesero)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")

        self.verticalLayout_11.addLayout(self.horizontalLayout_9)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_4)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.Mesero_1 = QPushButton(self.Pagina_SeleccionMesero)
        self.Mesero_1.setObjectName(u"Mesero_1")
        self.Mesero_1.setMinimumSize(QSize(100, 50))

        self.verticalLayout_10.addWidget(self.Mesero_1)

        self.Mesero_2 = QPushButton(self.Pagina_SeleccionMesero)
        self.Mesero_2.setObjectName(u"Mesero_2")
        self.Mesero_2.setMinimumSize(QSize(100, 50))

        self.verticalLayout_10.addWidget(self.Mesero_2)

        self.Mesero_3 = QPushButton(self.Pagina_SeleccionMesero)
        self.Mesero_3.setObjectName(u"Mesero_3")
        self.Mesero_3.setMinimumSize(QSize(100, 50))

        self.verticalLayout_10.addWidget(self.Mesero_3)

        self.Mesero_4 = QPushButton(self.Pagina_SeleccionMesero)
        self.Mesero_4.setObjectName(u"Mesero_4")
        self.Mesero_4.setMinimumSize(QSize(100, 50))

        self.verticalLayout_10.addWidget(self.Mesero_4)

        self.Mesero_5 = QPushButton(self.Pagina_SeleccionMesero)
        self.Mesero_5.setObjectName(u"Mesero_5")
        self.Mesero_5.setMinimumSize(QSize(200, 50))

        self.verticalLayout_10.addWidget(self.Mesero_5)


        self.horizontalLayout_8.addLayout(self.verticalLayout_10)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setSpacing(30)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.lineEdit_6 = QLineEdit(self.Pagina_SeleccionMesero)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setMinimumSize(QSize(0, 40))

        self.verticalLayout_9.addWidget(self.lineEdit_6)

        self.lineEdit_NombreUsuario_2 = QLineEdit(self.Pagina_SeleccionMesero)
        self.lineEdit_NombreUsuario_2.setObjectName(u"lineEdit_NombreUsuario_2")
        self.lineEdit_NombreUsuario_2.setMinimumSize(QSize(0, 40))

        self.verticalLayout_9.addWidget(self.lineEdit_NombreUsuario_2)

        self.lineEdit_FuncionUsuario_2 = QLineEdit(self.Pagina_SeleccionMesero)
        self.lineEdit_FuncionUsuario_2.setObjectName(u"lineEdit_FuncionUsuario_2")
        self.lineEdit_FuncionUsuario_2.setMinimumSize(QSize(0, 40))

        self.verticalLayout_9.addWidget(self.lineEdit_FuncionUsuario_2)

        self.lineEdit_ContrasenaUsuario_3 = QLineEdit(self.Pagina_SeleccionMesero)
        self.lineEdit_ContrasenaUsuario_3.setObjectName(u"lineEdit_ContrasenaUsuario_3")
        self.lineEdit_ContrasenaUsuario_3.setMinimumSize(QSize(0, 40))

        self.verticalLayout_9.addWidget(self.lineEdit_ContrasenaUsuario_3)

        self.lineEdit_ContrasenaUsuario_2 = QLineEdit(self.Pagina_SeleccionMesero)
        self.lineEdit_ContrasenaUsuario_2.setObjectName(u"lineEdit_ContrasenaUsuario_2")
        self.lineEdit_ContrasenaUsuario_2.setMinimumSize(QSize(0, 40))

        self.verticalLayout_9.addWidget(self.lineEdit_ContrasenaUsuario_2)


        self.horizontalLayout_8.addLayout(self.verticalLayout_9)


        self.verticalLayout_11.addLayout(self.horizontalLayout_8)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_3)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_14 = QLabel(self.Pagina_SeleccionMesero)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(0, 50))

        self.horizontalLayout_7.addWidget(self.label_14)

        self.label_3 = QLabel(self.Pagina_SeleccionMesero)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_7.addWidget(self.label_3)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_5)

        self.Boton_AceptarModificarUsuario = QPushButton(self.Pagina_SeleccionMesero)
        self.Boton_AceptarModificarUsuario.setObjectName(u"Boton_AceptarModificarUsuario")
        self.Boton_AceptarModificarUsuario.setMinimumSize(QSize(300, 100))

        self.horizontalLayout_7.addWidget(self.Boton_AceptarModificarUsuario)


        self.verticalLayout_11.addLayout(self.horizontalLayout_7)

        self.stacked_controlPaginas.addWidget(self.Pagina_SeleccionMesero)
        self.layoutWidget = QWidget(self.pagina_usuarios)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 10, 1121, 131))
        self.Layout_UsuariosCRUD = QHBoxLayout(self.layoutWidget)
        self.Layout_UsuariosCRUD.setSpacing(19)
        self.Layout_UsuariosCRUD.setObjectName(u"Layout_UsuariosCRUD")
        self.Layout_UsuariosCRUD.setContentsMargins(9, 9, 9, 9)
        self.Boton_Mesas = QPushButton(self.layoutWidget)
        self.Boton_Mesas.setObjectName(u"Boton_Mesas")
        self.Boton_Mesas.setMinimumSize(QSize(80, 100))

        self.Layout_UsuariosCRUD.addWidget(self.Boton_Mesas)

        self.Boton_Restaurantes = QPushButton(self.layoutWidget)
        self.Boton_Restaurantes.setObjectName(u"Boton_Restaurantes")
        self.Boton_Restaurantes.setMinimumSize(QSize(80, 100))

        self.Layout_UsuariosCRUD.addWidget(self.Boton_Restaurantes)

        self.Boton_Comida = QPushButton(self.layoutWidget)
        self.Boton_Comida.setObjectName(u"Boton_Comida")
        self.Boton_Comida.setMinimumSize(QSize(80, 100))

        self.Layout_UsuariosCRUD.addWidget(self.Boton_Comida)

        self.Boton_SeleccionMesero = QPushButton(self.layoutWidget)
        self.Boton_SeleccionMesero.setObjectName(u"Boton_SeleccionMesero")
        self.Boton_SeleccionMesero.setMinimumSize(QSize(80, 100))
        self.Boton_SeleccionMesero.setMaximumSize(QSize(300, 16777215))

        self.Layout_UsuariosCRUD.addWidget(self.Boton_SeleccionMesero)

        self.stacked_Menu.addWidget(self.pagina_usuarios)

        self.verticalLayout_4.addWidget(self.stacked_Menu)


        self.horizontalLayout_2.addWidget(self.frame_contenido)


        self.verticalLayout_2.addWidget(self.frame_inferior)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 9)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stacked_Menu.setCurrentIndex(0)
        self.stacked_controlPaginas.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Boton_menu.setText("")
        self.Boton_minimizar.setText("")
        self.Boton_restaurar.setText("")
        self.Boton_maximizar.setText("")
        self.Boton_cerrar.setText("")
        self.Boton_Atras.setText(QCoreApplication.translate("MainWindow", u"ATRAS", None))
        self.Boton_comfirmarPedido.setText(QCoreApplication.translate("MainWindow", u"COMFIRMAR PEDIDO", None))
        self.Producto_3.setText(QCoreApplication.translate("MainWindow", u"Producto 3", None))
        self.Mesa2_4.setText(QCoreApplication.translate("MainWindow", u"Producto 1", None))
        self.Producto_2.setText(QCoreApplication.translate("MainWindow", u"Producto 2", None))
        self.Boton_ImprimirFactura.setText(QCoreApplication.translate("MainWindow", u"Imprimir", None))
        self.Boton_NotaDelProducto.setText(QCoreApplication.translate("MainWindow", u"Nota", None))
        self.Boton_DescartarPedido.setText(QCoreApplication.translate("MainWindow", u"Descartar", None))
        self.Boton_Total.setText(QCoreApplication.translate("MainWindow", u"Total", None))
#if QT_CONFIG(whatsthis)
        self.Boton_AgregarProducto.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\">libre</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.Boton_AgregarProducto.setText(QCoreApplication.translate("MainWindow", u"Agregar Producto", None))
#if QT_CONFIG(whatsthis)
        self.Boton_Cantidad.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\">libre</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.Boton_Cantidad.setText(QCoreApplication.translate("MainWindow", u"Cantidad", None))
        self.Restaurante_3.setText(QCoreApplication.translate("MainWindow", u"Restaurante 3", None))
        self.Restaurante_2.setText(QCoreApplication.translate("MainWindow", u"Restaurante 2", None))
        self.Restaurante_1.setText(QCoreApplication.translate("MainWindow", u"Restaurante 1", None))
        self.Mesa12.setText(QCoreApplication.translate("MainWindow", u"LIBRE", None))
        self.Mesa2.setText(QCoreApplication.translate("MainWindow", u"LIBRE", None))
        self.Mesa8.setText(QCoreApplication.translate("MainWindow", u"LIBRE", None))
        self.Mesa7.setText(QCoreApplication.translate("MainWindow", u"LIBRE", None))
        self.Mesa9.setText(QCoreApplication.translate("MainWindow", u"LIBRE", None))
#if QT_CONFIG(whatsthis)
        self.Mesa1.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\">libre</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.Mesa1.setText(QCoreApplication.translate("MainWindow", u"LIBRE", None))
        self.Mesa10.setText(QCoreApplication.translate("MainWindow", u"LIBRE", None))
        self.Mesa5.setText(QCoreApplication.translate("MainWindow", u"LIBRE", None))
        self.Mesa4.setText(QCoreApplication.translate("MainWindow", u"LIBRE", None))
        self.Mesa11.setText(QCoreApplication.translate("MainWindow", u"LIBRE", None))
        self.Mesa3.setText(QCoreApplication.translate("MainWindow", u"LIBRE", None))
        self.Mesa6.setText(QCoreApplication.translate("MainWindow", u"LIBRE", None))
        self.Mesero_1.setText(QCoreApplication.translate("MainWindow", u"Mesero 1", None))
        self.Mesero_2.setText(QCoreApplication.translate("MainWindow", u"Mesero 2", None))
        self.Mesero_3.setText(QCoreApplication.translate("MainWindow", u"Mesero 3", None))
        self.Mesero_4.setText(QCoreApplication.translate("MainWindow", u"Mesero 4 ", None))
        self.Mesero_5.setText(QCoreApplication.translate("MainWindow", u"Mesero 5", None))
        self.label_14.setText("")
        self.label_3.setText("")
        self.Boton_AceptarModificarUsuario.setText(QCoreApplication.translate("MainWindow", u"SELECCIONAR MESERO", None))
        self.Boton_Mesas.setText(QCoreApplication.translate("MainWindow", u"MESAS", None))
        self.Boton_Restaurantes.setText(QCoreApplication.translate("MainWindow", u"RESTAURANTES", None))
        self.Boton_Comida.setText(QCoreApplication.translate("MainWindow", u"COMIDA", None))
        self.Boton_SeleccionMesero.setText(QCoreApplication.translate("MainWindow", u"SELECCION MESERO", None))
    # retranslateUi

