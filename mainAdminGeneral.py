import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QSizeGrip, QGraphicsDropShadowEffect, QMessageBox
from PyQt5.QtCore import Qt, QPropertyAnimation, QEasingCurve
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic
from PyQt5.uic import loadUi

class VentanaAdmingeneral(QMainWindow):
    def __init__(self,):
        super(VentanaAdmingeneral,self).__init__()
        QMainWindow.__init__(self)
        uic.loadUi("C:\POOGrafic\mockub\AdminGeneral.ui", self) 

        # Configuración de la ventana
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowOpacity(1)

        # Tamaño del grip
        self.gripSize = 10
        self.grip = QSizeGrip(self)
        self.grip.resize(self.gripSize, self.gripSize)

        # Mover ventana
        self.frame_superior.mouseMoveEvent = self.mover_ventana

        # Acceder a las páginas
        
        self.Boton_cerrarAbrirDia.clicked.connect(lambda: self.stacked_Menu.setCurrentWidget(self.pagina_AbrirCerrarDia_2))
        self.Boton_cerrarSesion.clicked.connect(lambda: self.stacked_Menu.setCurrentWidget(self.pagina_CerrarSesion))
        self.Boton_pedidos.clicked.connect(lambda: self.stacked_Menu.setCurrentWidget(self.pagina_Pedidos))
        self.Boton_productos.clicked.connect(lambda: self.stacked_Menu.setCurrentWidget(self.pagina_Productos))
        self.Boton_resumenVentas.clicked.connect(lambda: self.stacked_Menu.setCurrentWidget(self.pagina_ResumenV))
        self.Boton_locales.clicked.connect(lambda: self.stacked_Menu.setCurrentWidget(self.pagina_locales))
        self.Boton_usuarios.clicked.connect(lambda: self.stacked_Menu.setCurrentWidget(self.pagina_usuarios))

        #Acceder menu productos
        self.Boton_AgregarProducto.clicked.connect(lambda: self.stacked_PaginaProductos.setCurrentWidget(self.Pagina_AgregarProductos))
        self.Boton_EliminarProducto.clicked.connect(lambda: self.stacked_PaginaProductos.setCurrentWidget(self.Pagina_EliminarProductos))
        self.Boton_ModificarProducto.clicked.connect(lambda: self.stacked_PaginaProductos.setCurrentWidget(self.Pagina_ModificarProducto))

        #Acceder menu locales
        self.Boton_AgregarLocal.clicked.connect(lambda: self.stacked_PaginaLocal.setCurrentWidget(self.Pagina_AgregarLocal))
        self.Boton_EliminarLocal_2.clicked.connect(lambda: self.stacked_PaginaLocal.setCurrentWidget(self.Pagina_EliminarLocal))
        self.Boton_ModificarLocal.clicked.connect(lambda: self.stacked_PaginaLocal.setCurrentWidget(self.Pagina_ModificarLocal))

        #Acceder menu usuarios
        self.Boton_AgregarUsuario.clicked.connect(lambda: self.stacked_PaginaUsuario.setCurrentWidget(self.Pagina_AgregarUsuario))
        self.Boton_EliminarUsuario.clicked.connect(lambda: self.stacked_PaginaUsuario.setCurrentWidget(self.Pagina_EliminarUsuario))
        self.Boton_ModificaUsuario.clicked.connect(lambda: self.stacked_PaginaUsuario.setCurrentWidget(self.Pagina_ModificarUsuario))



        # Control de menú
        self.Boton_menu.clicked.connect(self.mover_menu)    

        # Control de ventana
        self.Boton_minimizar.clicked.connect(self.showMinimized)
        self.Boton_cerrar.clicked.connect(self.close)
        self.Boton_maximizar.clicked.connect(self.showMaximized)
        self.Boton_restaurar.clicked.connect(self.showNormal)


    def restaurar(self):
        self.showNormal()
        self.Boton_maximizar.show()
        self.Boton_restaurar.hide()

    def maximizar(self):
        self.showMaximized()
        self.Boton_restaurar.show()
        self.Boton_maximizar.hide()

    def showMinimizar(self):
        self.showMinimized()
        self.Boton_restaurar.show()


    def mover_menu(self):
            if True:			
                    width = self.frame_control.width()
                    normal = 0
                    if width==0:
                        extender = 300
                    else:
                        extender = normal
                    self.animacion = QPropertyAnimation(self.frame_control, b'minimumWidth')
                    self.animacion.setDuration(300)
                    self.animacion.setStartValue(width)
                    self.animacion.setEndValue(extender)
                    self.animacion.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
                    self.animacion.start()

    def mover_ventana(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
    
    def resizeEvent(self, event):
        rect = self.rect()
        self.grip.move(rect.right() - self.gripSize, rect.bottom() - self.gripSize)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = VentanaAdmingeneral()
    ventana.show()

    sys.exit(app.exec_())
