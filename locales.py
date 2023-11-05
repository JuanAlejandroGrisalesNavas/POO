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
                local = cursor.fetchone()
                if local:
                    print("Local encontrado:")
                    print("Nombre del local:", local[0])
                else:
                    print("Local no encontrado.")
        except psycopg2.Error as e:
            print("Ocurrió un error al buscar el local: ", e)
            return False
        
    def actualizarLocal(self, conexion, nombre_local):
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT * FROM locales WHERE nombre_local = %s", (nombre_local,))
                local = cursor.fetchone()
                if local:
                    print("Local encontrado: ")
                    print("Nombre local:", local[0])

                    cambiosLocal = {}
                    cambiosLocal["nuevo_nombre_local"] = input("Nuevo nombre del local: ")

                    confirmacion = input("¿Desea aplicar estos cambios? (S/N): ").strip().lower()

                    if confirmacion == "s":
                        with conexion.cursor() as cursor:
                            cursor.execute("UPDATE locales SET nombre_local = %s WHERE nombre_local = %s", (cambiosLocal["nuevo_nombre_local"], nombre_local))
                            conexion.commit()
                        print("Local actualizado exitosamente.")
                    else:
                        print("Cambios no aplicados.")
                else:
                    print("El local no existe")
        except psycopg2.Error as e:
            print("Ocurrió un error al consultar o actualizar el local: ", e)