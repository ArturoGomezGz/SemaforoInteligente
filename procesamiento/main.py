import sys
sys.path.append(r"../")
from clases.interseccion import Interseccion
from clases.semaforo import Semaforo
import json
import os
import requests


semaforo1 = Semaforo(
    json.loads(requests.get("http://127.0.0.1:5000/semaforo/1").json())[0],
    )
print("Semaforo 1 creado")

semaforo2 = Semaforo(
    json.loads(requests.get("http://127.0.0.1:5000/semaforo/2").json())[0],
    )
print("Semaforo 2 creado")

interseccion1 = Interseccion(
    json.loads(requests.get("http://127.0.0.1:5000/interseccion/1").json())[0],
    [semaforo1, semaforo2], 
    )
print("Interseccion 1 creada")

interseccion1.procesar()
interseccion1.ajustarTiempo()



