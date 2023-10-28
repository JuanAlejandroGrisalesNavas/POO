import psycopg2
from productos import *

class Pedido(Producto):
    mesa = ""

    def __init__(self, nombre_producto, id_producto, precio_producto, local_pert, mesa):
        super().__init__(nombre_producto, id_producto, precio_producto, local_pert)
        self.mesa = mesa

    def agregarProductos(self, conexion, nombre_producto, id_producto, precio_producto, local_pert, mesa):


    def modificarProductos(self, conexion, nombre_producto, id_producto, precio_producto, local_pert, mesa):


    def generarFactura