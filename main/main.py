import semaforo

semaforo1 = semaforo.Semaforo()
semaforo1.ruta_video = "../resources/video1.mp4"
semaforo1.detecta_carros()

semaforo1.imprime()
semaforo1.exportaJson()