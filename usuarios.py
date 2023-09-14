import psycopg2

class usuario():
    id = ""
    nombre = ""
    apellido = ""
    documento = ""

    def __init__(self, nombre, apellido, documento):
        self.nombre = nombre
        self.apellido = apellido
        self.documento = documento

    def imprimirNombre(self):
        print("El nombre del usuario es ", self.nombre)

    def crearUsuario(self, conexion, nombre, apellido):
        try:
            with conexion.cursor() as cursor:
                consulta = "INSERT INTO usuarios(nombre, apellido) VALUES (%s, %s);"
                cursor.execute(consulta, (nombre, apellido))
            conexion.commit()
            return True
        except psycopg2.Error as e:
            print("Ocurrió un error al crear el usuario: ", e)
            return False
        
    def leerUsuarios(self, conexion):
        try:
            with conexion.cursor() as cursor:
                consulta = "SELECT * FROM usuarios;"
                cursor.execute(consulta)
                usuarios = cursor.fetchall()
                for usuario in usuarios:
                    print("ID:", usuario[0])
                    print("Nombre:", usuario[1])
                    print("Apellido:", usuario[2])
                    print("Documento:", usuario[3])
        except psycopg2.Error as e:
            print("Ocurrió un error al leer los usuarios:", e)

    def eliminarUsuario(self, conexion, nombre, apellido):
        try:
            with conexion.cursor() as cursor:
                consulta = "DELETE FROM usuarios WHERE nombre = %s AND apellido = %s;"
                cursor.execute(consulta, (nombre, apellido))
            conexion.commit()
            return True
        except psycopg2.Error as e:
            print("Ocurrió un error al eliminar el usuario: ", e)
            return False
        
    def buscarUsuario(self, conexion, nombre, apellido):
        try:
            with conexion.cursor() as cursor:
                consulta = "SELECT FROM usuarios WHERE nombre = %s AND apellido = %s;"
                cursor.execute(consulta, (nombre, apellido))
            conexion.commit()
            return True
        except psycopg2.Error as e:
            print("Ocurrió un error al buscar el usuario: ", e)
            return False    
