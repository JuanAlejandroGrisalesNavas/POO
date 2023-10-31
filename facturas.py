import psycopg2
from productos import Producto

class Factura(Producto):
    fecha = ""
    cant_Productos = 0
    mesero = ""
    mesa = ""
    total_Pagar = 0.0

    def __init__(self, nombre_producto, precio_producto, local_pert, fecha, cant_Productos, mesero, mesa, total_Pagar):
        super().__init__(nombre_producto, precio_producto, local_pert)
        self.fecha = fecha
        self.cant_Productos = cant_Productos
        self.mesero = mesero
        self.mesa = mesa
        self.total_Pagar = total_Pagar

    def imprimir(self):
        print("Factura")
        print("Fecha:", self.fecha)
        print("Mesero:", self.mesero)
        print("Mesa:", self.mesa)
        print("Productos comprados:")
        super().leerProductos(self.conexion)  # Utiliza el método leerProductos de la clase Producto para mostrar los productos
        print("Total a pagar: $", self.total_Pagar)