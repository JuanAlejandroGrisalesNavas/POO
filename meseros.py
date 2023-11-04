import psycopg2
from usuarios import *

class Mesero(Usuario):

    def __init__(self, nombre, apellido, documento, usuario, contrasena, rol):
        super().__init__(nombre, apellido, documento, usuario, contrasena, rol)
    """
    Revisar el funcionamiento de las funciones
    def iniciarServicio():

    def modificarPedido():

    def modificarPedidoListo():

    def cerrarServicio():

    def facturar():
    """