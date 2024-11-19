import sys
sys.path.append(r"../")
from conexion.conexion import Conexion
import json
from clases.semaforo import Semaforo
import os

with open('../dbData.json', 'r') as archivo:
    baseDeDatos = json.load(archivo)

conection = Conexion(baseDeDatos)



semaforo1 = Semaforo(
    json.loads(conection.getSemaforo(1))[0]["id"],
    json.loads(conection.getSemaforo(1))[0]["tVerde"],
    json.loads(conection.getSemaforo(1))[0]["tRojo"],
    "resources/video1.mp4",
    json.loads(conection.getSemaforo(1))[0]["rutaVideo"]
    )

semaforo2 = Semaforo(
    json.loads(conection.getSemaforo(2))[0]["id"],
    json.loads(conection.getSemaforo(2))[0]["tVerde"],
    json.loads(conection.getSemaforo(2))[0]["tRojo"],
    "resources/video2.mp4",
    json.loads(conection.getSemaforo(2))[0]["rutaVideo"]
    )

semaforo1.print()
semaforo2.print()

semaforo1.recortarVideo()
semaforo2.recortarVideo()

conection.cerrarConexion()