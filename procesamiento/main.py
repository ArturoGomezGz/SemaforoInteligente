import sys
sys.path.append(r"../")
from conexion.conexion import Conexion
from clases.interseccion import Interseccion
from clases.semaforo import Semaforo
import json
import os


with open('../dbData.json', 'r') as archivo:
    baseDeDatos = json.load(archivo)

conection = Conexion(baseDeDatos)

semaforo1 = Semaforo(
    json.loads(conection.getSemaforo(1))[0],
    baseDeDatos
    )
print("Semaforo 1 creado")

semaforo2 = Semaforo(
    json.loads(conection.getSemaforo(2))[0],
    baseDeDatos
    )
print("Semaforo 2 creado")

interseccion1 = Interseccion(
    json.loads(conection.getInterseccion(1))[0],
    [semaforo1, semaforo2], 
    baseDeDatos
    )
print("Interseccion 1 creada")

conection.cerrarConexion()

for i in range(0,2):
    interseccion1.procesar()
    interseccion1.ajustarTiempo()



