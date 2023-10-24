import psycopg2

class Producto():
    nombre_producto = ""
    id_producto = ""
    precio_producto = ""
    local_pert = ""

    def __init__(self, nombre_producto, id_producto, precio_producto, local_pert):
        self.nombre_producto = nombre_producto
        self.id_producto = id_producto
        self.precio_producto = precio_producto
        self.local_pert = local_pert

    def crearProducto(self, conexion, nombre_producto, id_producto, precio_producto, local_pert):
        try:
            with conexion.cursor() as cursor:
                consulta = "INSERT INTO productos(nombre_producto, id_producto, precio_producto, local_pert) VALUES (%s, %s);"
                cursor.execute(consulta, (nombre_producto, id_producto, precio_producto, local_pert))
            conexion.commit()
            return True
        except psycopg2.Error as e:
            print("Ocurrió un error al crear el producto")

    def leerProductos(self, conexion):
        try:
            with conexion.cursor() as cursor:
                consulta = "SELECT * FROM productos;"
                cursor.execute(consulta)
                productos = cursor.fetchall()
                for producto in productos:
                    print("Nombre: ", producto[0])
                    print("id_producto: ", producto[1])
                    print("Precio por producto: ", producto[2])
                    print("Local: ", producto[3])
        except psycopg2.Error as e:
            print("Ocurrió un error al leer los productos")
    
    def eliminarProducto(self, conexion, nombre_producto, id_producto, precio_producto, local_pert):
        try:
            with conexion.cursor() as cursor:
                consulta = "DELETE FROM productos WHERE nombre_producto = %s;"
                cursor.execute(consulta, (nombre_producto, id_producto, precio_producto, local_pert))
            conexion.commit()
            return True
        except psycopg2.Error as e:
            print("Ocurrió un error al eliminar el producto: ", e)
            return False
        
    def buscarProducto(self, conexion, nombre_producto, id_producto, precio_producto, local_pert):
        try:
            with conexion.cursor() as cursor:
                consulta = "SELECT FROM productos WHERE nombre_producto = %s;"
                cursor.execute(consulta, (nombre_producto, id_producto, precio_producto, local_pert))
            conexion.commit()
            return True
        except psycopg2.Error as e:
            print("Ocurrió un error al buscar el producto: ", e)
            return False
        
    def actualizarProducto(self, conexion, nombre_producto, id_producto, precio_producto, local_pert):
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT * FROM productos WHERE nombre_producto = %s", (nombre_producto))
                producto = cursor.fetchone()
                if producto:
                    print("Producto encontrado:")
                    print(producto)

                    cambios = {}
                    cambios["nuevo_nombre_producto"] = input("Nombre producto a modificar: ")
                    cambios["nuevo_id_producto"] = input("Id producto a modificar: ")
                    cambios["nuevo_precio_producto"] = input("Precio a modificar: ")
                    
                    confirmacion = input("¿Desea aplicar estos cambios? (S/N): ").strip().lower()

                    if confirmacion == "s":
                        with conexion.cursor() as cursor:
                            cursor.execute("UPDATE productos SET nombre_producto = %s, id_producto = %s, precio_producto = %s WHERE nombre_producto = %s", (cambios["nuevo_nombre_producto"], cambios["nuevo_id_producto"], cambios["nuevo_precio_producto"]))
                            conexion.commit()
                        print("Producto actualizado exitosamenete.")
                    else:
                        print("Cambios no aplicados.")
                else:
                    print("El producto no existe")
        except psycopg2.Error as e:
            print("Ocurrió un error al consultar o actualizar el producto: ", e)