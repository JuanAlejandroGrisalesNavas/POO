import psycopg2
from usuarios import *

class Cocinero(Usuario):
    local = ""

    def __init__(self,nombre, apellido, documento, usuario, contrasena, rol, local):
        super().__init__(nombre, apellido, documento, usuario, contrasena, rol)
        self.local = local
    """
    Revisar el funcionamiento de las siguientes funciones
    def recibirNotificaciones():
        
    def aceptarPedidos():
    """