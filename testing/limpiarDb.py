from conexion.conexion import Conexion
import json

baseDeDatos = {
    "server" : "localhost",  # Cambia esto a tu servidor SQL
    "database" : "SemaforoInteligente",  # Cambia esto a tu base de datos
    "usuario" : "arturo",
    "contrasena" : "Pword1",
}

conection = Conexion(baseDeDatos)

conection.limpiarRegistros()

conection.cerrarConexion()




