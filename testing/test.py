import sys
sys.path.append(r"../")
from conexion.conexion import Conexion
import json
import time
import os
import pymysql

with open('../dbData.json', 'r') as archivo:
    baseDeDatos = json.load(archivo)

conection = Conexion(baseDeDatos)

data = conection.getSemaforo(1)
print(data)

conection.cerrarConexion()




