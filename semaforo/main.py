import sys
sys.path.append(r"../")
from clases.semaforoConPines import SemaforoConPines
from clases.interseccion import Interseccion
import json 
import requests
import time

""" jsonSemaforo1 = {
    "id": 1,
    "tVerde": 30,
    "tRojo": 30,
    "rutaVideo": "/ruta/del/video",
    "rutaCascade": "/ruta/del/cascade",
    "salidaY": 200,
    "scaleFactor": 1.1,
    "minNeighbors": 5,
    "minSize": (30, 30),
    "maxSize": (300, 300)
}
jsonSemaforo2 = {
    "id": 2,
    "tVerde": 30,
    "tRojo": 30,
    "rutaVideo": "/ruta/del/video",
    "rutaCascade": "/ruta/del/cascade",
    "salidaY": 200,
    "scaleFactor": 1.1,
    "minNeighbors": 5,
    "minSize": (30, 30),
    "maxSize": (300, 300)
} """

jsonInterseccion1 = {
  "id": 1,
  "noSemaforos": 3,
  "tCiclo": 60,
}


pinesS1 = {
    "redPin": 2,
    "greenPin": 3,
    "yellowPin": 4
}
pinesS2 = {
    "redPin": 4,
    "greenPin": 5,
    "yellowPin": 6
}

semaforo1 = SemaforoConPines(
    json.loads(requests.get("http://127.0.0.1:5000/semaforo/1").json())[0],
    pinesS1
    )
print("Semaforo 1 creado")

semaforo2 = SemaforoConPines(
    json.loads(requests.get("http://127.0.0.1:5000/semaforo/2").json())[0],
    pinesS2
    )
print("Semaforo 2 creado")

interseccion1 = Interseccion(
    json.loads(requests.get("http://127.0.0.1:5000/interseccion/1").json())[0],
    [semaforo1, semaforo2], 
    )
print("Interseccion 1 creada")


for i in range(2):
    semaforo1.encender_verde()
    time.sleep(int(semaforo1.tVerde)-5)
    semaforo1.encender_amarillo()
    time.sleep(5)
    semaforo1.encender_rojo()
    time.sleep(int(semaforo1.tRojo))