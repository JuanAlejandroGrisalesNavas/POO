import psycopg2

class Producto():
    nombre_producto = ""
    id_producto = ""
    precio_producto = ""
    disponibilidad = ""
    local_pert = ""

    def __init__(self, nombre_producto, id_producto, precio_producto, disponibilidad, local_pert):
        self.nombre_producto = nombre_producto
        self.id_producto = id_producto
        self.precio_producto = precio_producto
        self.disponibilidad = disponibilidad
        self.local_pert = local_pert

    def crearProducto(self, conexion, nombre_producto, id_producto, precio_producto, disponibilidad, local_pert):
        try:
            with conexion.cursor() as cursor:
                consulta = "INSERT INTO productos(nombre_producto, id_producto, precio_producto, disponibilidad, local_pert) VALUES (%s, %s);"
                cursor.execute(consulta, (nombre_producto, id_producto, precio_producto, disponibilidad, local_pert))
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
                    print("Nombre: ", producto[0])
                    print("id_producto: ", producto[1])
                    print("Precio por producto: ", producto[2])
                    print("Disponibilidad producto: ", producto[3])
                    print("Local: ", producto[4])
        except psycopg2.Error as e:
            print("Ocurrió un error al leer los productos")
    
    def eliminarProducto(self, conexion, nombre_producto, id_producto, precio_producto, disponibilidad, local_pert):
        