from clases.interseccion import Interseccion
from clases.semaforo import Semaforo
from conexion.conexion import Conexion

server = "DESKTOP-GI8HMHT"  # Cambia esto a tu servidor SQL
database = "SemaforoInteligente"  # Cambia esto a tu base de datos

conection = Conexion(server = server, database = database)
conection.establecerConexion()

datosS1 = conection.leer("Semaforo", "WHERE id = 1")[0]
datosS2 = conection.leer("Semaforo", "WHERE id = 2")[0]

conection.cerrarConexion()

semaforo1 = Semaforo(
    idSemaforo = datosS1[0], 
    ruta_video = datosS1[3], 
    dbServer = server, 
    dbDatabase = database
    )

semaforo2 = Semaforo(
    idSemaforo = datosS2[0], 
    ruta_video = datosS2[3], 
    dbServer = server, 
    dbDatabase = database
    )

interseccion1 = Interseccion([semaforo1, semaforo2])

interseccion1.procesar()
interseccion1.ajustarTiempo()



