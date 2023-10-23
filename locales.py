import psycopg2

class Local():
    nombre = ""
    producto = ""
    cantProducto = ""

    def __init__(self, nombre, producto, cantProducto):
        self.nombre = nombre
        self.producto = producto
        self.cantProducto = cantProducto

    def crearLocal(self, conexion, nombre, producto, cantProducto):
        try:
            with conexion.cursor() as cursor:
                consulta = "INSERT INTO locales(nombre, producto, cantProducto) VALUEs (%s,%s);"
                cursor.execute(consulta, (nombre, producto, cantProducto))
            conexion.commit()
            return True
        except psycopg2.Error as e:
            print("Ocurrió un error al crear el local: ", e)
            return False
        
    def leerLocales(self, conexion):
        try:
            with conexion.cursor() as cursor:
                consulta = "SELECT * FROM locales"
                cursor.execute(consulta)
                locales = cursor.fetchall()
                for local in locales:
                    print("NOMBRE: ", locales[0])
        except psycopg2.Error as e:
            print("Ocurrió un error al leer los locales: ", e)

    def eliminarLocal(self, conexion, nombre):
        try:
            with conexion.cursor() as cursor:
                consulta = "DELETE FROM locales WHERE nombre = %s;"
                cursor.execute(consulta, (nombre))
            conexion.commit()
            return True
        except psycopg2.Error as e:
            print("Ocurrió un error al eliminar el local: ", e)
            return False
        
    def buscarLocal(self, conexion, nombre):
        try:
            with conexion.cursor() as cursor:
                consulta = "SELECT FROM locales WHERE nombre = %;"
                cursor.execute(consulta, (nombre))
            conexion.commit()
            return True
        except psycopg2.Error as e:
            print("Ocurrió un error al buscar el local: ", e)
            return False