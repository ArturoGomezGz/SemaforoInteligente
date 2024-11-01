from clases.interseccion import Interseccion
from clases.semaforo import Semaforo
import conexion.conexion

semaforo1 = Semaforo(idSemaforo = 1, ruta_video = "resources/video1.mp4", dbServer = "DESKTOP-GI8HMHT", dbDatabase = "SemaforoInteligente")
semaforo2 = Semaforo(idSemaforo = 2, ruta_video = "resources/video2.mp4", dbServer = "DESKTOP-GI8HMHT", dbDatabase = "SemaforoInteligente")

interseccion1 = Interseccion([semaforo1, semaforo2])

interseccion1.procesar()
interseccion1.ajustarTiempo()



