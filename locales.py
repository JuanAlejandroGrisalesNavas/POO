import psycopg2

class Local():
    nombre_local = ""

    def __init__(self, nombre_local):
        self.nombre_local = nombre_local

    def crearLocal(self, conexion, nombre_local):
        try:
            with conexion.cursor() as cursor:
                consulta = "INSERT INTO locales(nombre_local) VALUES (%s);"
                cursor.execute(consulta, (nombre_local,))
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
                    print("NOMBRE:", local[0])
        except psycopg2.Error as e:
            print("Ocurrió un error al leer los locales: ", e)

    def eliminarLocal(self, conexion, nombre_local):
        try:
            with conexion.cursor() as cursor:
                consulta = "DELETE FROM locales WHERE nombre_local = %s;"
                cursor.execute(consulta, (nombre_local,))
            conexion.commit()
            return True
        except psycopg2.Error as e:
            print("Ocurrió un error al eliminar el local: ", e)
            return False
        
    def buscarLocal(self, conexion, nombre_local):
        try:
            with conexion.cursor() as cursor:
                consulta = "SELECT * FROM locales WHERE nombre_local = %s;"
                cursor.execute(consulta, (nombre_local,))
            conexion.commit()
            return True
        except psycopg2.Error as e:
            print("Ocurrió un error al buscar el local: ", e)
            return False