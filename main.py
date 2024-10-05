from clases.semaforo import Semaforo

semaforo1 = Semaforo()
semaforo1.ruta_video = "resources/video1.mp4"
semaforo1.detecta_carros()

semaforo1.imprime()
semaforo1.exportaJson()