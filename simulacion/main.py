import sys
sys.path.append(r"../")
from clases.interseccion import Interseccion
from clases.semaforoSimulacion import SemaforoSimulacion
import json
import os
import requests

semaforo1 = SemaforoSimulacion(
    json.loads(requests.get("http://127.0.0.1:5000/semaforo/1").json())[0],
    "resources/video1.mp4"
    )
print("Semaforo 1 creado")

semaforo2 = SemaforoSimulacion(
    json.loads(requests.get("http://127.0.0.1:5000/semaforo/2").json())[0],
    "resources/video2.mp4"
    )
print("Semaforo 2 creado")

interseccion1 = Interseccion(
    json.loads(requests.get("http://127.0.0.1:5000/interseccion/1").json())[0],
    [semaforo1, semaforo2], 
    )
print("Interseccion 1 creada")

semaforo1.imprime()
semaforo2.imprime()

semaforo1.recortarVideo()
semaforo2.recortarVideo()
