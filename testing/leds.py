import sys
sys.path.append(r"../")
from clases.semaforoConPines import SemaforoConPines
from clases.interseccion import Interseccion
import json 
import requests
import time

pinesS1 = {
    "redPin": 3,
    "greenPin": 5,
    "yellowPin": 7
}
""" pinesS2 = {
    "redPin": 18,
    "greenPin": 23,
    "yellowPin": 24
} """

semaforo1 = SemaforoConPines(
    json.loads(requests.get("http://127.0.0.1:5000/semaforo/1").json())[0],
    pinesS1
    )
print("Semaforo 1 creado")

""" semaforo2 = SemaforoConPines(
    json.loads(requests.get("http://127.0.0.1:5000/semaforo/2").json())[0],
    pinesS2
    )
print("Semaforo 2 creado") """

""" interseccion1 = Interseccion(
    json.loads(requests.get("http://127.0.0.1:5000/interseccion/1").json())[0],
    [semaforo1, semaforo2], 
    )
print("Interseccion 1 creada") """


semaforo1.encender_rojo()
""" semaforo2.encender_rojo() """

time.sleep(3)

semaforo1.encender_amarillo()
""" semaforo2.encender_amarillo() """

time.sleep(3)

semaforo1.encender_verde()
""" semaforo2.encender_verde() """