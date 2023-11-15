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
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
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
        self.Boton_resumenVentas = QPushButton(self.frame_control)
        self.Boton_resumenVentas.setObjectName(u"Boton_resumenVentas")
        self.Boton_resumenVentas.setMinimumSize(QSize(40, 70))
        self.Boton_resumenVentas.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.Boton_resumenVentas)

        self.tableView = QTableView(self.frame_control)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout_3.addWidget(self.tableView)

        self.Boton_cerrarSesion = QPushButton(self.frame_control)
        self.Boton_cerrarSesion.setObjectName(u"Boton_cerrarSesion")
        self.Boton_cerrarSesion.setMinimumSize(QSize(0, 120))
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
        self.stacked_PaginaUuario = QStackedWidget(self.pagina_usuarios)
        self.stacked_PaginaUuario.setObjectName(u"stacked_PaginaUuario")
        self.stacked_PaginaUuario.setGeometry(QRect(10, 150, 1131, 571))
        self.Pagina_AgregarUsuario = QWidget()
        self.Pagina_AgregarUsuario.setObjectName(u"Pagina_AgregarUsuario")
        self.verticalLayout_8 = QVBoxLayout(self.Pagina_AgregarUsuario)
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
        self.Mesa2_3 = QPushButton(self.Pagina_AgregarUsuario)
        self.Mesa2_3.setObjectName(u"Mesa2_3")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Mesa2_3.sizePolicy().hasHeightForWidth())
        self.Mesa2_3.setSizePolicy(sizePolicy)
        self.Mesa2_3.setStyleSheet(u"QPushButton{\n"
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

        self.gridLayout_2.addWidget(self.Mesa2_3, 1, 3, 1, 1)

        self.Mesa3_2 = QPushButton(self.Pagina_AgregarUsuario)
        self.Mesa3_2.setObjectName(u"Mesa3_2")
        sizePolicy.setHeightForWidth(self.Mesa3_2.sizePolicy().hasHeightForWidth())
        self.Mesa3_2.setSizePolicy(sizePolicy)
        self.Mesa3_2.setStyleSheet(u"QPushButton{\n"
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

        self.gridLayout_2.addWidget(self.Mesa3_2, 1, 6, 1, 1)

        self.Mesa2_2 = QPushButton(self.Pagina_AgregarUsuario)
        self.Mesa2_2.setObjectName(u"Mesa2_2")
        sizePolicy.setHeightForWidth(self.Mesa2_2.sizePolicy().hasHeightForWidth())
        self.Mesa2_2.setSizePolicy(sizePolicy)
        self.Mesa2_2.setStyleSheet(u"QPushButton{\n"
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

        self.gridLayout_2.addWidget(self.Mesa2_2, 1, 4, 1, 1)


        self.verticalLayout_6.addLayout(self.gridLayout_2)


        self.Layout_AgregarUsuario.addLayout(self.verticalLayout_6)


        self.verticalLayout_8.addLayout(self.Layout_AgregarUsuario)

        self.stacked_PaginaUuario.addWidget(self.Pagina_AgregarUsuario)
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
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Mesa1.sizePolicy().hasHeightForWidth())
        self.Mesa1.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setFamilies([u"Yu Gothic UI Semibold"])
        font.setPointSize(15)
        font.setWeight(QFont.)
        font.setItalic(False)
        font.setStrikeOut(False)
        font.setStyleStrategy(QFont.PreferDefault)
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
        icon5 = QIcon()
        icon5.addFile(u"../Users/holan/OneDrive/Escritorio/tabla.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Mesa1.setIcon(icon5)
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

        self.stacked_PaginaUuario.addWidget(self.Pagina_Mesas)
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
        self.pushButton_4 = QPushButton(self.Pagina_SeleccionMesero)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(100, 50))

        self.verticalLayout_10.addWidget(self.pushButton_4)

        self.pushButton_3 = QPushButton(self.Pagina_SeleccionMesero)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(100, 50))

        self.verticalLayout_10.addWidget(self.pushButton_3)

        self.pushButton = QPushButton(self.Pagina_SeleccionMesero)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(100, 50))

        self.verticalLayout_10.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.Pagina_SeleccionMesero)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(100, 50))

        self.verticalLayout_10.addWidget(self.pushButton_2)

        self.pushButton_5 = QPushButton(self.Pagina_SeleccionMesero)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(200, 50))

        self.verticalLayout_10.addWidget(self.pushButton_5)


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
        self.Boton_AceptarModificarUsuario.setMinimumSize(QSize(90, 30))

        self.horizontalLayout_7.addWidget(self.Boton_AceptarModificarUsuario)


        self.verticalLayout_11.addLayout(self.horizontalLayout_7)

        self.stacked_PaginaUuario.addWidget(self.Pagina_SeleccionMesero)
        self.layoutWidget = QWidget(self.pagina_usuarios)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 10, 1121, 131))
        self.Layout_UsuariosCRUD = QHBoxLayout(self.layoutWidget)
        self.Layout_UsuariosCRUD.setSpacing(19)
        self.Layout_UsuariosCRUD.setObjectName(u"Layout_UsuariosCRUD")
        self.Layout_UsuariosCRUD.setContentsMargins(9, 9, 9, 9)
        self.Boton_AgregarUsuario = QPushButton(self.layoutWidget)
        self.Boton_AgregarUsuario.setObjectName(u"Boton_AgregarUsuario")
        self.Boton_AgregarUsuario.setMinimumSize(QSize(80, 100))

        self.Layout_UsuariosCRUD.addWidget(self.Boton_AgregarUsuario)

        self.Boton_ModificaUsuario = QPushButton(self.layoutWidget)
        self.Boton_ModificaUsuario.setObjectName(u"Boton_ModificaUsuario")
        self.Boton_ModificaUsuario.setMinimumSize(QSize(80, 100))

        self.Layout_UsuariosCRUD.addWidget(self.Boton_ModificaUsuario)

        self.Boton_ModificaUsuario_2 = QPushButton(self.layoutWidget)
        self.Boton_ModificaUsuario_2.setObjectName(u"Boton_ModificaUsuario_2")
        self.Boton_ModificaUsuario_2.setMinimumSize(QSize(80, 100))

        self.Layout_UsuariosCRUD.addWidget(self.Boton_ModificaUsuario_2)

        self.Boton_EliminarUsuario = QPushButton(self.layoutWidget)
        self.Boton_EliminarUsuario.setObjectName(u"Boton_EliminarUsuario")
        self.Boton_EliminarUsuario.setMinimumSize(QSize(80, 100))
        self.Boton_EliminarUsuario.setMaximumSize(QSize(300, 16777215))

        self.Layout_UsuariosCRUD.addWidget(self.Boton_EliminarUsuario)

        self.stacked_Menu.addWidget(self.pagina_usuarios)

        self.verticalLayout_4.addWidget(self.stacked_Menu)


        self.horizontalLayout_2.addWidget(self.frame_contenido)


        self.verticalLayout_2.addWidget(self.frame_inferior)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 9)
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
        self.Boton_resumenVentas.setText(QCoreApplication.translate("MainWindow", u"ATRAS", None))
        self.Boton_cerrarSesion.setText(QCoreApplication.translate("MainWindow", u"COMFIRMAR PEDIDO", None))
        self.Mesa2_3.setText(QCoreApplication.translate("MainWindow", u"Restaurante 1", None))
        self.Mesa3_2.setText(QCoreApplication.translate("MainWindow", u"Restaurante 3", None))
        self.Mesa2_2.setText(QCoreApplication.translate("MainWindow", u"Restaurante 2", None))
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
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label_14.setText("")
        self.label_3.setText("")
        self.Boton_AceptarModificarUsuario.setText(QCoreApplication.translate("MainWindow", u"Aceptar", None))
        self.Boton_AgregarUsuario.setText(QCoreApplication.translate("MainWindow", u"MESAS", None))
        self.Boton_ModificaUsuario.setText(QCoreApplication.translate("MainWindow", u"RESTAURANTES", None))
        self.Boton_ModificaUsuario_2.setText(QCoreApplication.translate("MainWindow", u"COMIDA", None))
        self.Boton_EliminarUsuario.setText(QCoreApplication.translate("MainWindow", u"SELECCION MESERO", None))
    # retranslateUi

