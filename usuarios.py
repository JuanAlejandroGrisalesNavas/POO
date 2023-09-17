import psycopg2

class Usuario():
    id = ""
    nombre = ""
    apellido = ""
    documento = ""
    usuario = ""
    contrasena = ""

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


    #update
    def actualizarUsuario(self, conexion, nombre, apellido):
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT * FROM usuarios WHERE nombre=%s", (nombre,))
                usuario = cursor.fetchone()
                if usuario:
                    print("Usuario encontrado:")
                    print(usuario)

                    cambios = {}
                    cambios["nuevo_nombre"] = input("Nombre usuario a modificar: ")
                    cambios["nuevo_apellido"] = input("Apellido usuario a modificar: ")

                    confirmacion = input("¿Desea aplicar estos cambios? (S/N): ").strip().lower()

                    if confirmacion == "s":
                        with conexion.cursor() as cursor:
                            cursor.execute("UPDATE usuarios SET nombre=%s, apellido=%s WHERE nombre=%s", (cambios["nuevo_nombre"], cambios["nuevo_apellido"], nombre))
                            conexion.commit()
                        print("Usuario actualizado exitosamente.")
                    else:
                        print("Cambios no aplicados.")
                else:
                    print("El usuario no existe")
        except psycopg2.Error as e:
            print("Ocurrió un error al consultar o actualizar el usuario: ", e)
    
    #login
    def login(self,conexion,usuario,contrasena):
        try:
            with conexion.cursor() as cursor:
                consulta = "SELECT * FROM usuarios WHERE usuario = %s AND contrasena = %s;"
                cursor.execute(consulta, (usuario, contrasena))
                usuario = cursor.fetchone()
                if usuario:
                    print("Bienvenido ", usuario[1])
                    return True
                else:
                    print("Usuario o contraseña incorrectos")
                    return False
        except psycopg2.Error as e:
            print("Ocurrió un error al buscar el usuario:", e)
            return False

    #close
    def close(self,conexion):
        try:
            conexion.close()
            print("Conexion cerrada")
        except psycopg2.Error as e:
            print("Ocurrió un error al cerrar la conexión:", e)
            return False