from clases.semaforo import Semaforo

semaforo1 = Semaforo(idSemaforo = 1, ruta_video = "resources/video1.mp4")
semaforo2 = Semaforo(idSemaforo = 2, ruta_video = "resources/video2.mp4")

semaforo1.detecta_carros()
semaforo2.detecta_carros()

semaforo1.exportaJson()
semaforo2.exportaJson()