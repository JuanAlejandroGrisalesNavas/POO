import psycopg2

class Basedatos():
    host = ""
    port = 5432
    user = ""
    password = ""
    database = ""

    def __init__(self,host,user,port,password,database):
        self.host = host
        self.user = user
        self.password = password
        self.port = port
        self.database = database

    def conectar(self):
        try:
            credenciales = {
                "dbname":self.database,
                "user":self.user,
                "password":self.password,
                "host":self.host,
                "port":self.port
            }
            conexion = psycopg2.connect(**credenciales)
            if conexion:
                print("Conexion exitosa a ",self.port)

            return conexion
        except psycopg2.Error as e:
            print("Ocurrio un error al conectar a PostgreSQL: ", e)