from basededatos import *
from usuarios import *
conexion = Basedatos("berry.db.elephantsql.com", "abaqcznm" ,5432, "Dk0tzRMVhrtWii2GzIoxqPlcjvq50dBn", "abaqcznm")
conexionExitosa = conexion.conectar()

usuario1 = Usuario("Pepito", "Perez", "123456789")
usuario2 = Usuario("Andres", "Perez", "987654321")

usuario1.imprimirNombre()
usuario1.nombre = "Otro"
usuario1.imprimirNombre()

usuario1.crearUsuario(conexionExitosa, "Pepito", "Perez")
#leer, editar
#usuario1.eliminarUsuario(conexionExitosa, "Pepito", "Perez")
#usuario1.leerUsuarios(conexionExitosa)