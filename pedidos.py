import psycopg2
from productos import Producto

class Pedido(Producto):
    mesa = ""

    def __init__(self, nombre_producto, precio_producto, local_pert, mesa):
        super().__init__(nombre_producto, precio_producto, local_pert)
        self.mesa = mesa

    def agregarProductos(self, conexion, nombre_producto, precio_producto, local_pert, cantidad):
        try:
            with conexion.cursor() as cursor:
                consulta = "INSERT INTO pedidos(nombre_producto, precio_producto, local_pert, mesa, cantidad) VALUES (%s, %s, %s, %s, %s);"
                cursor.execute(consulta, (nombre_producto, precio_producto, local_pert, self.mesa, cantidad))
            conexion.commit()
            return True
        except psycopg2.Error as e:
            print("Ocurrió un error al agregar producto al pedido:", e)
            return False

    def modificarProductos(self, conexion, nombre_producto, precio_producto, local_pert, nueva_cantidad):
        try:
            with conexion.cursor() as cursor:
                consulta = "UPDATE pedidos SET cantidad = %s WHERE nombre_producto = %s AND mesa = %s;"
                cursor.execute(consulta, (nueva_cantidad, nombre_producto, self.mesa))
            conexion.commit()
            return True
        except psycopg2.Error as e:
            print("Ocurrió un error al modificar producto en el pedido:", e)
            return False

    def generarFactura(self, conexion):
        try:
            with conexion.cursor() as cursor:
                consulta = "SELECT nombre_producto, precio_producto, cantidad FROM pedidos WHERE mesa = %s;"
                cursor.execute(consulta, (self.mesa,))
                productos_pedido = cursor.fetchall()

                total = 0
                print("Factura para la mesa", self.mesa)
                for producto in productos_pedido:
                    nombre, precio, cantidad = producto
                    subtotal = precio * cantidad
                    total += subtotal
                    print(f"{nombre}: {cantidad} x ${precio} = ${subtotal}")

                print("Total a pagar: $", total)
        except psycopg2.Error as e:
            print("Ocurrió un error al generar la factura:", e)