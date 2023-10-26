import psycopg2
from productos import *

class Factura(Producto):
    fecha = ""
    cant_Productos = ""
    mesero = ""
    mesa = ""
    total_Pagar = ""
    metodo_Pago = ""

    def __init__(self, nombre_producto, precio_unitario, local_pert, fecha, cant_Productos, mesero, mesa, total_Pagar, metodo_Pago):
        self.nombre_producto = nombre_producto
        self.precio_producto = precio_unitario
        self.local_pert = local_pert
        self.fecha = fecha
        self. cant_Productos = cant_Productos
        self.mesero = mesero
        self.mesa = mesa
        self.total_Pagar = total_Pagar
        self.metodo_Pago = metodo_Pago