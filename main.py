from basededatos import *
from usuarios import *

#conexion =Basedatos("berry.db.elephantsql.com", "zcogoady" ,5432, "cQlAt2_pKmQf5QGpBTr8tNyHKqGjwfVg", "zcogoady")
#conexionExitosa = conexion.conectar()

#usuario1 = usuario("Juanito", "Navas", "2456378")
#usuario2 = usuario("Vane", "Montoya", "9786756")

#usuario1.imprimirNombre()
#usuario1.imprimirNombre()

#usuario1.crearUsuario(conexionExitosa, "Juanito", "Navas")
#usuario2.crearUsuario(conexionExitosa, "Vane", "Montoya")

#Crear, leer, editar y eliminar

#usuario1.eliminarUsuario(conexionExitosa, "Vane", "Montoya")
#usuario1.leerUsuarios(conexionExitosa)

#usuario1.buscarUsuario(conexionExitosa, "Juanito", "Navas")


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
    print("3. Iniciar sesión")
    print("4. Actualizar usuario")
    print("5. Eliminar usuario")
    print("6. Cerrar conexión")
    print("0. Salir")
    opcion = input("Seleccione una opción: ")
    return opcion


if __name__ == "__main__":
    conexion = conectar_bd()
    uasuearios = usuario("", "", "")

    while True:
        opcion = mostrar_menu()

        if opcion == "1":
            nombre = input("Nombre del usuario: ")
            apellido = input("Apellido del usuario: ")
            uasuearios.crearUsuario(conexion, nombre, apellido)

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
                usuario1.actualizarUsuario(conexion, nuevo_nombre, nuevo_apellido)
            else:
                print("Debe conectar a la base de datos primero.")

        elif opcion == "5":
            if conexion is not None:
                nombre = input("Nombre del usuario a eliminar: ")
                apellido = input("Apellido del usuario a eliminar: ")
                usuario1.eliminarUsuario(conexion, nombre, apellido)
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

        elif opcion == "0":
            if conexion is not None:
                conexion.close()
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

