from basededatos import *
from usuarios import *

conexion =Basedatos("berry.db.elephantsql.com", "zcogoady" ,5432, "cQlAt2_pKmQf5QGpBTr8tNyHKqGjwfVg", "zcogoady")
conexionExitosa = conexion.conectar()

usuario1 = usuario("Juanito", "Navas", "2456378")
usuario2 = usuario("Vane", "Montoya", "9786756")

usuario1.imprimirNombre()
usuario1.imprimirNombre()

#usuario1.crearUsuario(conexionExitosa, "Juanito", "Navas")
#usuario2.crearUsuario(conexionExitosa, "Vane", "Montoya")

#Crear, leer, editar y eliminar

#usuario1.eliminarUsuario(conexionExitosa, "Vane", "Montoya")
#usuario1.leerUsuarios(conexionExitosa)

usuario1.buscarUsuario(conexionExitosa, "Juanito", "Navas")
