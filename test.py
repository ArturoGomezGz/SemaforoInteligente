from conexion.conexion import Conexion
import json
import time
import os
import pymysql

baseDeDatos = {
    "server" : "10.43.125.45",  # Cambia esto a tu servidor SQL
    "database" : "SemaforoInteligente",  # Cambia esto a tu base de datos
    "usuario" : "arturo",
    "contrasena" : "Pword1",
    "port": 3306
}

conection = Conexion(baseDeDatos)

data = conection.getSemaforo(1)
print(data)

conection.cerrarConexion()




