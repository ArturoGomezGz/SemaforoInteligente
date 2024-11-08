from conexion.conexion import Conexion
import json
import time
import os

baseDeDatos = {
    "server" : "localhost",  # Cambia esto a tu servidor SQL
    "database" : "SemaforoInteligente",  # Cambia esto a tu base de datos
    "usuario" : "arturo",
    "contrasena" : "Pword1",
}

conection = Conexion(baseDeDatos)

conection.ajustarTiempoSemaforo(1,30,20)
data = conection.getSemaforo(1)
print(data)

conection.cerrarConexion()




