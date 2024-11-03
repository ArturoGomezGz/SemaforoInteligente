from clases.interseccion import Interseccion
from clases.semaforo import Semaforo
from conexion.conexion import Conexion

baseDeDatos = {
    "driver" : "SQL Server",
    "server" : "DESKTOP-GI8HMHT",  # Cambia esto a tu servidor SQL
    "database" : "SemaforoInteligente",  # Cambia esto a tu base de datos
    "usuario" : "",
    "contrasena" : "",
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

interseccion1.procesar()
interseccion1.ajustarTiempo()



