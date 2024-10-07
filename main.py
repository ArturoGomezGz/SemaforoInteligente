from clases.interseccion import Interseccion
from clases.semaforo import Semaforo

semaforo1 = Semaforo(idSemaforo = 1, ruta_video = "resources/video1.mp4", ruta_cascade="classifier/haarcascade_car.xml", scaleFactor=1.5, minNeighbors=9)
semaforo2 = Semaforo(idSemaforo = 2, ruta_video = "resources/video2.mp4", ruta_cascade="classifier/haarcascade_car.xml")

interseccion1 = Interseccion([semaforo1, semaforo2])

interseccion1.procesar()
interseccion1.ajustarTiempo()

