from clases.interseccion import Interseccion
from clases.semaforo import Semaforo
from conexion.conexion import Conexion
import json

baseDeDatos = {
    "server" : "localhost",  # Cambia esto a tu servidor SQL
    "database" : "SemaforoInteligente",  # Cambia esto a tu base de datos
    "usuario" : "arturo",
    "contrasena" : "Pword1",
}

conection = Conexion(baseDeDatos)

semaforo1 = Semaforo(
    json.loads(conection.getSemaforo(1))[0],
    baseDeDatos
    )

semaforo2 = Semaforo(
    json.loads(conection.getSemaforo(2))[0],
    baseDeDatos
    )

interseccion1 = Interseccion(
    json.loads(conection.getInterseccion(1))[0],
    [semaforo1, semaforo2], 
    baseDeDatos
    )

conection.cerrarConexion()

for i in range(0,2):
    interseccion1.procesar()
    interseccion1.ajustarTiempo()



