from clases.interseccion import Interseccion
from clases.semaforo import Semaforo
from conexion.conexion import Conexion

server = "DESKTOP-GI8HMHT"  # Cambia esto a tu servidor SQL
database = "SemaforoInteligente"  # Cambia esto a tu base de datos

conection = Conexion(server = server, database = database)
conection.establecerConexion()

datosS1 = conection.leer("Semaforo", "WHERE id = 1")
datosS2 = conection.leer("Semaforo", "WHERE id = 2")
datosI1 = conection.leer("Interseccion", "WHERE id = 1")

conection.cerrarConexion()

semaforo1 = Semaforo(
    idSemaforo = datosS1[0], 
    tVerde = datosS1[1],
    tRojo = datosS1[2],
    ruta_video = datosS1[3],
    ruta_cascade = datosS1[4],
    salida_y = datosS1[5],
    scaleFactor = datosS1[6],
    minNeighbors = datosS1[7],
    minSize = datosS1[8],
    maxSize = datosS1[9],
    dbServer = server, 
    dbDatabase = database
    )

semaforo2 = Semaforo(
    idSemaforo = datosS2[0], 
    tVerde = datosS2[1],
    tRojo = datosS2[2],
    ruta_video = datosS2[3],
    ruta_cascade = datosS2[4],
    salida_y = datosS2[5],
    scaleFactor = datosS2[6],
    minNeighbors = datosS2[7],
    minSize = datosS2[8],
    maxSize = datosS2[9],
    dbServer = server, 
    dbDatabase = database
    )

interseccion1 = Interseccion(
    idInterseccion = datosI1[0],
    tCiclo = datosI1[2],
    semaforos = [semaforo1, semaforo2], 
    dbServer = server, 
    dbDatabase = database
    )

interseccion1.procesar()
interseccion1.ajustarTiempo()



