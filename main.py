from clases.interseccion import Interseccion
from clases.semaforo import Semaforo
from conexion.conexion import Conexion

baseDeDatos = {
    "driver" : "SQL Server",
    "server" : "localhost",  # Cambia esto a tu servidor SQL
    "database" : "IoT",  # Cambia esto a tu base de datos
    "usuario" : "root",
    "contrasena" : "password",
}

conection = Conexion(baseDeDatos)

semaforo1 = Semaforo(
    conection.leer("Semaforo", "WHERE id = 1"),
    baseDeDatos
    )

semaforo2 = Semaforo(
    conection.leer("Semaforo", "WHERE id = 2"),
    baseDeDatos
    )

interseccion1 = Interseccion(
    conection.leer("Interseccion", "WHERE id = 1"),
    [semaforo1, semaforo2], 
    baseDeDatos
    )

conection.cerrarConexion()

for i in range(0,2):
    interseccion1.procesar()
    interseccion1.ajustarTiempo()



