import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QSizeGrip, QGraphicsDropShadowEffect, QMessageBox
from PyQt5.QtCore import Qt, QPropertyAnimation, QEasingCurve
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic
from PyQt5.uic import loadUi

class VentanaMeseros(QMainWindow):
    def __init__(self,):
        super(VentanaMeseros,self).__init__()
        QMainWindow.__init__(self)
        uic.loadUi("C:\POOGrafic\mockub\MeserosGrafic.ui", self) 

        # Configuración de la ventana
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowOpacity(1)

        # Tamaño del grip
        self.gripSize = 10
        self.grip = QSizeGrip(self)
        self.grip.resize(self.gripSize, self.gripSize)

        # Mover ventana
        self.frame_superior.mouseMoveEvent = self.mover_ventana



        # Control de menú
        self.Boton_menu.clicked.connect(self.mover_menu)    

        # Control de ventana
        self.Boton_minimizar.clicked.connect(self.showMinimized)
        self.Boton_cerrar.clicked.connect(self.close)
        self.Boton_maximizar.clicked.connect(self.showMaximized)
        self.Boton_restaurar.clicked.connect(self.showNormal)

        # Acceder a las páginas
        self.Boton_Mesas.clicked.connect(lambda: self.stacked_controlPaginas.setCurrentWidget(self.Pagina_Mesas))
        self.Boton_Restaurantes.clicked.connect(lambda: self.stacked_controlPaginas.setCurrentWidget(self.Pagina_Restaurantes))
        self.Boton_SeleccionMesero.clicked.connect(lambda: self.stacked_controlPaginas.setCurrentWidget(self.Pagina_SeleccionMesero))
        self.Boton_Comida.clicked.connect(lambda: self.stacked_controlPaginas.setCurrentWidget(self.Pagina_Comida))

        # Boton restaurante a comida
        self.Restaurante_1.clicked.connect(lambda: self.stacked_controlPaginas.setCurrentWidget(self.Pagina_Comida))
        self.Restaurante_2.clicked.connect(lambda: self.stacked_controlPaginas.setCurrentWidget(self.Pagina_Comida))
        self.Restaurante_3.clicked.connect(lambda: self.stacked_controlPaginas.setCurrentWidget(self.Pagina_Comida))
        
        # Boton mesas a restaurante
        self.Mesa1.clicked.connect(lambda: self.stacked_controlPaginas.setCurrentWidget(self.Pagina_Restaurantes))
        self.Mesa2.clicked.connect(lambda: self.stacked_controlPaginas.setCurrentWidget(self.Pagina_Restaurantes))
        self.Mesa3.clicked.connect(lambda: self.stacked_controlPaginas.setCurrentWidget(self.Pagina_Restaurantes))
        self.Mesa4.clicked.connect(lambda: self.stacked_controlPaginas.setCurrentWidget(self.Pagina_Restaurantes))
        self.Mesa5.clicked.connect(lambda: self.stacked_controlPaginas.setCurrentWidget(self.Pagina_Restaurantes))
        self.Mesa6.clicked.connect(lambda: self.stacked_controlPaginas.setCurrentWidget(self.Pagina_Restaurantes))
        self.Mesa7.clicked.connect(lambda: self.stacked_controlPaginas.setCurrentWidget(self.Pagina_Restaurantes))
        self.Mesa8.clicked.connect(lambda: self.stacked_controlPaginas.setCurrentWidget(self.Pagina_Restaurantes))
        self.Mesa9.clicked.connect(lambda: self.stacked_controlPaginas.setCurrentWidget(self.Pagina_Restaurantes))
        self.Mesa10.clicked.connect(lambda: self.stacked_controlPaginas.setCurrentWidget(self.Pagina_Restaurantes))
        self.Mesa11.clicked.connect(lambda: self.stacked_controlPaginas.setCurrentWidget(self.Pagina_Restaurantes))
        self.Mesa12.clicked.connect(lambda: self.stacked_controlPaginas.setCurrentWidget(self.Pagina_Restaurantes))




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
                        extender = 400
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
    ventana = VentanaMeseros()
    ventana.show()

    sys.exit(app.exec_())
