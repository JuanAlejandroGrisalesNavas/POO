from basededatos import *
from usuarios import *
from locales import *
from productos import *
from pedidos import *
from facturas import *

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
    print("3. Eliminar usuario")
    print("4. Buscar usuario")
    print("5. Actualizar usuario")
    print("6. Iniciar sesión")
    print("7. Cerrar conexión")
    print("8. Crear local")
    print("9. Leer locales")
    print("10. Eliminar local")
    print("11. Buscar local")
    print("12. Actualizar local")
    print("0. Salir")
    opcion = input("Seleccione una opción: ")
    return opcion

if __name__ == "__main__":
    conexion = conectar_bd()
    usuario1 = Usuario("", "", "", "", "", "")
    local1 = Local("")
    producto1 = Producto("", "", "", "")
    while True:
        opcion = mostrar_menu()

        if opcion == "1":
            nombre = input("Nombre del usuario: ")
            apellido = input("Apellido del usuario: ")
            documento = input("Documento del usuario: ")
            usuario = input("Usuario de la persona: ")
            contrasena = input("Contraseña del usuario: ")
            rol = input("Puesto del usuario: ")
            usuario1.crearUsuario(conexion, nombre, apellido, documento, usuario, contrasena, rol)

        elif opcion == "2":
            if conexion is not None:
                usuario1.leerUsuarios(conexion)
            else:
                print("Debe conectar a la base de datos primero.")

        elif opcion == "3":
            if conexion is not None:
                nombre = ""
                apellido = ""
                documento = input("Documento del usuario a eliminar: ")
                usuario = ""
                contrasena = ""
                rol = ""
                usuario1.eliminarUsuario(conexion, nombre, apellido, documento, usuario, contrasena, rol)
            else:
                print("El usuario no pudo ser eliminado.")

        elif opcion == "4":
            if conexion is not None:
                documento = input("Documento del usuario a buscar: ")
                usuario1.buscarUsuario(conexion, documento)
            else:
                print("No se pudo encontrar al usuario.")

        elif opcion == "5":
            if conexion is not None:
                documento = input("Documento del usuario a modificar: ")
                usuario1.actualizarUsuario(conexion, documento)
            else:
                print("No se pudo modificar el usuario.")
                
        elif opcion == "6":
            if conexion is not None:
                usuario = input("Nombre de usuario: ")
                contrasena = input("Contraseña: ")
                if usuario1.login(conexion, usuario, contrasena):
                    print("Inicio de sesión exitoso.")
                else:
                    print("Inicio de sesión fallido. Usuario o contraseña incorrectos.")
            else:
                print("Debe conectar a la base de datos primero.")

        elif opcion == "7":
            if conexion is not None:
                conexion.close()
                print("Conexión cerrada.")
                conexion = None
                usuario1 = None
            else:
                print("No hay conexión abierta.")
            
        elif opcion == "8":
            if conexion is not None:
                nombre_local = input("Nombre del local: ")
                local1.crearLocal(conexion, nombre_local)
            else:
                print("No se pudo crear el local.")

        elif opcion == "9":
            if conexion is not None:
                local1.leerLocales(conexion)
            else:
                print("No se pudo mostrar los locales.")

        elif opcion == "10":
            if conexion is not None:
                nombre_local = input("Nombre del local a eliminar: ")
                local1.eliminarLocal(conexion, nombre_local)
            else:
                print("No se pudo eliminar el local.")

        elif opcion == "11":
            if conexion is not None:
                nombre_local = input("Nombre del local a buscar: ")
                local1.buscarLocal(conexion, nombre_local)
            else:
                print("No se pudo encontrar el local.")

        elif opcion == "12":
            if conexion is not None:
                nuevo_nombre_local = input("Nombre del local a actualizar: ")
                local1.actualizarLocal(conexion, nuevo_nombre_local)
            else:
                print("No se pudo eliminar el local.")

        elif opcion == "0":
            if conexion is not None:
                conexion.close()
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intente de nuevo.")