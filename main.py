from basededatos import *
from usuarios import *
from locales import *

def conectar_bd():
    try:
        conexion = psycopg2.connect(
            host="berry.db.elephantsql.com",
            database="zcogoady",
            user="zcogoady",
            password="cQlAt2_pKmQf5QGpBTr8tNyHKqGjwfVg"
        )
        print("Conexión exitosa a la base de datos.")
        return conexion
    except psycopg2.Error as e:
        print("Error de conexión a la base de datos:", e)
        return None
    
def mostrar_menu():
    print("\n--- Menú de Funciones ---")
    print("1. Crear usuario")
    print("2. Leer usuarios")
#    print("3. Iniciar sesión")
    print("4. Actualizar usuario")
    print("5. Eliminar usuario")
    print("6. Cerrar conexión")
    print("7. Crear local")
    print("0. Salir")
    opcion = input("Seleccione una opción: ")
    return opcion

if __name__ == "__main__":
    conexion = conectar_bd()
    usuario1 = Usuario("", "", "", "", "")
    local1 = Local("", "", "")

    while True:
        opcion = mostrar_menu()

        if opcion == "1":
            nombre = input("Nombre del usuario: ")
            apellido = input("Apellido del usuario: ")
            documento = input("Documento del usuario: ")
            usuario = input("Usuario de la persona: ")
            contrasena = input("Contraseña del usuario: ")
            usuario1.crearUsuario(conexion, nombre, apellido, documento, usuario, contrasena)

        elif opcion == "2":
            if conexion is not None:
                usuario1.leerUsuarios(conexion)
            else:
                print("Debe conectar a la base de datos primero.")

#        elif opcion == "3":
#            if conexion is not None:
#                nombre_usuario = input("Nombre de usuario: ")
#                contrasena = input("Contraseña: ")
#                if usuario1.login(conexion, nombre_usuario, contrasena):
#                    print("Inicio de sesión exitoso.")
#                else:
#                    print("Inicio de sesión fallido. Usuario o contraseña incorrectos.")
#            else:
#                print("Debe conectar a la base de datos primero.")

        elif opcion == "4":
            if conexion is not None:
                nuevo_nombre = input("Nuevo nombre: ")
                nuevo_apellido = input("Nuevo apellido: ")
                nuevo_usuario = input("Nuevo usuario: ")
                nueva_contrasena = input("Nueva contraseña")
                usuario1.actualizarUsuario(conexion, nuevo_nombre, nuevo_apellido, nuevo_usuario, nueva_contrasena)
            else:
                print("Debe conectar a la base de datos primero.")

        elif opcion == "5":
            if conexion is not None:
                nombre = input("Nombre del usuario a eliminar: ")
                apellido = input("Apellido del usuario a eliminar: ")
                usuario1.eliminarUsuario(conexion, nombre, apellido, documento, usuario, contrasena)
            else:
                print("Debe conectar a la base de datos primero.")

        elif opcion == "6":
            if conexion is not None:
                conexion.close()
                print("Conexión cerrada.")
                conexion = None
                usuario1 = None
            else:
                print("No hay conexión abierta.")
            
        elif opcion == "7":
            if conexion is not None:
                nombre = input("Nombre del local: ")
                producto = input("Nombre producto: ")
                cantProducto = input("Cantidad producto: ")
                local1.crearLocal(conexion, nombre, producto, cantProducto)


        elif opcion == "0":
            if conexion is not None:
                conexion.close()
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intente de nuevo.")