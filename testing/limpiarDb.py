import sys
sys.path.append(r"../")
from conexion.conexion import Conexion
import json

with open('../dbData.json', 'r') as archivo:
    baseDeDatos = json.load(archivo)

conection = Conexion(baseDeDatos)

conection.limpiarRegistros()

conection.cerrarConexion()




