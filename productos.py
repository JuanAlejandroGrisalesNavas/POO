import psycopg2

class Producto():
    nombre_producto = ""
    id_producto = ""
    precio_producto = ""
    disponibilidad = ""

    def __init__(self, nombre_producto, id_producto, precio_producto, disponibilidad):
        self.nombre_producto = nombre_producto
        self.id_producto = id_producto
        self.precio_producto = precio_producto
        self.disponibilidad = disponibilidad

    def crearProducto(self, conexion, nombre_producto, id_producto, precio_producto, disponibilidad):
        try:
            with conexion.cursor() as cursor:
                consulta = "INSERT INTO productos(nombre_producto, id_producto, precio_producto, disponibilidad) VALUES (%s, %s);"
                cursor.execute(consulta, (nombre_producto, id_producto, precio_producto, disponibilidad))
            conexion.commit()
            return True
        except psycopg2.Error as e:
            print("Ocurrió un error al crear el producto")

    def leerProductos(self, conexion):
        try:
            with conexion.cursor() as cursor:
                consulta = "SELECT * FROM productos;"
                cursor.execute(consulta)
                productos = cursor.fetchall()
                for producto in productos:
                    print("Nombre: ", producto)