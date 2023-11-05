import psycopg2

class Usuario:
    def __init__(self, nombre, apellido, documento, usuario, contrasena, rol):
        self.nombre = nombre
        self.apellido = apellido
        self.documento = documento
        self.usuario = usuario
        self.contrasena = contrasena
        self.rol = rol

    def crearUsuario(self, conexion, nombre, apellido, documento, usuario, contrasena, rol):
        try:
            with conexion.cursor() as cursor:
                consulta = "SELECT * FROM usuarios WHERE documento = %s;"
                cursor.execute(consulta, (documento,))
                usuario = cursor.fetchone()
                if usuario:
                    print("Ya existe un usuario con ese numero de documento.")
                else:
                    consulta = "INSERT INTO usuarios (nombre, apellido, documento, usuario, contrasena, rol) VALUES (%s, %s, %s, %s, %s, %s);"
                    cursor.execute(consulta, (nombre, apellido, documento, usuario, contrasena, rol))
                    print("Usuario creado exitosamente.")
            conexion.commit()
            return True
        except psycopg2.Error as e:
            print("Ocurrió un error al crear el usuario:", e)
            return False

    def leerUsuarios(self, conexion):
        try:
            with conexion.cursor() as cursor:
                consulta = "SELECT * FROM usuarios;"
                cursor.execute(consulta)
                usuarios = cursor.fetchall()
                for usuario in usuarios:
                    print("Nombre:", usuario[0])
                    print("Apellido:", usuario[1])
                    print("Documento:", usuario[2])
                    print("Usuario:", usuario[3])
                    print("Contraseña:", usuario[4])
                    print("Puesto:", usuario[5])
        except psycopg2.Error as e:
            print("Ocurrió un error al leer los usuarios:", e)

    def eliminarUsuario(self, conexion, nombre, apellido, documento, usuario, contrasena, rol):
        try:
            with conexion.cursor() as cursor:
                consulta = "DELETE FROM usuarios WHERE documento = %s;"
                cursor.execute(consulta, (documento,))
            conexion.commit()
            print("Usuario eliminado exitosamente.")
            return True
        except psycopg2.Error as e:
            print("Ocurrió un error al eliminar el usuario:", e)
            return False

    def buscarUsuario(self, conexion, documento):
        try:
            with conexion.cursor() as cursor:
                consulta = "SELECT * FROM usuarios WHERE documento = %s;"
                cursor.execute(consulta, (documento,))
                usuario = cursor.fetchone()
                if usuario:
                    print("Usuario encontrado:")
                    print("Nombre:", usuario[0])
                    print("Apellido:", usuario[1])
                    print("Documento:", usuario[2])
                    print("Usuario:", usuario[3])
                    print("Contraseña:", usuario[4])
                    print("Puesto:", usuario[5])
                else:
                    print("Usuario no encontrado.")
        except psycopg2.Error as e:
            print("Ocurrió un error al buscar el usuario:", e)

    def actualizarUsuario(self, conexion, documento):
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT * FROM usuarios WHERE documento = %s", (documento,))
                usuario = cursor.fetchone()
                if usuario:
                    print("Usuario encontrado:")
                    print("Nombre:", usuario[0])
                    print("Apellido:", usuario[1])
                    print("Documento:", usuario[2])
                    print("Usuario:", usuario[3])
                    print("Contraseña:", usuario[4])
                    print("Puesto:", usuario[5])

                    cambios = {}
                    cambios["nuevo_nombre"] = input("Nuevo nombre del usuario: ")
                    cambios["nuevo_apellido"] = input("Nuevo apellido del usuario: ")
                    cambios["nuevo_usuario"] = input("Nuevo usuario: ")
                    cambios["nueva_contrasena"] = input("Nueva contraseña: ")

                    confirmacion = input("¿Desea aplicar estos cambios? (S/N): ").strip().lower()

                    if confirmacion == "s":
                        with conexion.cursor() as cursor:
                            cursor.execute("UPDATE usuarios SET nombre = %s, apellido = %s, usuario = %s, contrasena = %s WHERE documento = %s", (cambios["nuevo_nombre"], cambios["nuevo_apellido"], cambios["nuevo_usuario"], cambios["nueva_contrasena"], documento))
                            conexion.commit()
                        print("Usuario actualizado exitosamente.")
                    else:
                        print("Cambios no aplicados.")
                else:
                    print("El usuario no existe.")
        except psycopg2.Error as e:
            print("Ocurrió un error al consultar o actualizar el usuario:", e)

    def login(self, conexion, usuario, contrasena):
        try:
            with conexion.cursor() as cursor:
                consulta = "SELECT * FROM usuarios WHERE usuario = %s AND contrasena = %s;"
                cursor.execute(consulta, (usuario, contrasena))
                usuario = cursor.fetchone()
                if usuario:
                    print("Bienvenido, " + usuario[0])
                    return True
                else:
                    print("Usuario o contraseña incorrectos.")
                    return False
        except psycopg2.Error as e:
            print("Ocurrió un error al buscar el usuario:", e)
            return False

    def close(self, conexion):
        try:
            conexion.close()
            print("Conexión cerrada.")
        except psycopg2.Error as e:
            print("Ocurrió un error al cerrar la conexión:", e)
            return False