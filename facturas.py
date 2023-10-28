import psycopg2
from productos import *

class Factura(Producto):
    fecha = ""
    cant_Productos = ""
    mesero = ""
    mesa = ""
    total_Pagar = ""
    metodo_Pago = ""

    def __init__(self, nombre_producto, precio_producto, local_pert, fecha, cant_Productos, mesero, mesa, total_Pagar, metodo_Pago):
        super().__init__(nombre_producto, precio_producto, local_pert)
        self.fecha = fecha
        self. cant_Productos = cant_Productos
        self.mesero = mesero
        self.mesa = mesa
        self.total_Pagar = total_Pagar
        self.metodo_Pago = metodo_Pago

    def imprimir(self, nombre_producto, precio_producto, local_pert, fecha, cant_Productos, mesero, mesa, total_Pagar, metodo_Pago):