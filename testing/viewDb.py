from conexion.conexion import Conexion
import json
import time
import os

with open('../dbData.json', 'r') as archivo:
    baseDeDatos = json.load(archivo)

conection = Conexion(baseDeDatos)
os.system("clear")

print("mCiclos --------------------------------------")
json_data = conection.getMCiclos()
data = json.loads(json_data)
for i in data:
    print(i)
print("")

print("dCiclos --------------------------------------")
json_data = conection.getDCiclos()
data = json.loads(json_data)
for i in data:
    print(i)
print("")

print("Semaforos --------------------------------------")
json_data = conection.getSemaforos()
data = json.loads(json_data)
for i in data:
    print(i)
print("")

print("Interseciones --------------------------------------")
json_data = conection.getIntersecciones()
data = json.loads(json_data)
for i in data:
    print(i)
print("")

conection.cerrarConexion()




