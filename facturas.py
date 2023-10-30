import psycopg2
from productos import Producto

class Factura(Producto):
    fecha = ""
    cant_Productos = 0  # Inicializado a 0
    mesero = ""
    mesa = ""
    total_Pagar = 0.0  # Inicializado a 0.0
    metodo_Pago = ""

    def __init__(self, nombre_producto, precio_producto, local_pert, fecha, cant_Productos, mesero, mesa, total_Pagar, metodo_Pago):
        super().__init__(nombre_producto, precio_producto, local_pert)
        self.fecha = fecha
        self.cant_Productos = cant_Productos
        self.mesero = mesero
        self.mesa = mesa
        self.total_Pagar = total_Pagar
        self.metodo_Pago = metodo_Pago

    def imprimir(self):
        print("Factura")
        print("Fecha:", self.fecha)
        print("Mesero:", self.mesero)
        print("Mesa:", self.mesa)
        print("Productos comprados:")
        super().leerProductos(self.conexion)  # Utiliza el método leerProductos de la clase Producto para mostrar los productos
        print("Total a pagar: $", self.total_Pagar)
        print("Método de pago:", self.metodo_Pago)