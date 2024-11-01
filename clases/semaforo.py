import cv2
import json
import os
from conexion.conexion import Conexion

class Semaforo:
    def __init__(self, idSemaforo = 0, tVerde = 0, tRojo = 0, no_carros = 0, ruta_video = "", ruta_cascade = "classifier/cascade.xml", salida_y = 200, scaleFactor = 4, minNeighbors = 50, minSize = 50, maxSize = 100, dbDriver = "SQL Server", dbServer = "", dbDatabase = "", dbUsuario = "", dbContrasena = "" ):
        # Datos necesarios para la conexion a la db
        self.dbDriver = dbDriver
        self.dbServer = dbServer
        self.dbDatabase = dbDatabase
        self.dbUsuario = dbUsuario
        self.dbContrasena = dbContrasena

        self.idSemaforo = idSemaforo
        self.tVerde = tVerde # Tiempo (en segundos) en verde (ulitmos 5 segundo son amarillo)
        self.tRojo = tRojo # Tiempo en rojo (en segundos)
        self.no_carros = no_carros # Numero de carros acumilado en el ultimo rojo
        self.ruta_video = ruta_video # Ruta del video para el conteo de carros
        self.ruta_cascade = ruta_cascade # Ruta del archivo cascade (modelo de vision artificial)
        self.salida_y = salida_y # Numero de pixeles desde arriba (en y) para contar carros
        self.scaleFactor = scaleFactor  # Reduce la imagen en un 10% en cada escala; ajustar para más o menos detecciones
        self.minNeighbors = minNeighbors   # Número mínimo de vecinos para considerar una detección válida; ajustar según la precisión deseada
        self.minSize = minSize  # Tamaño mínimo de los objetos a detectar; ajustar según el tamaño esperado de los coches
        self.maxSize = maxSize  # Tamaño máximo de los objetos a detectar; establecer si quieres limitar el tamaño máximo
    
    def imprime(self):
        print(f"Numero de carros: {self.no_carros}")
        print(f"Tiempo en verde: {self.tVerde}")
        print(f"Tiempo en alto: {self.tRojo}")

    def detecta_carros(self):
        car_cascade = cv2.CascadeClassifier(self.ruta_cascade)
        cap = cv2.VideoCapture(self.ruta_video)

        detected_cars = {}  # Diccionario para almacenar las posiciones de autos rastreados (id: posición)

        #Bucle while que itera frame por frame 
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Detección de autos en el frame actual
            cars = car_cascade.detectMultiScale(
                gray, 
                scaleFactor=self.scaleFactor, 
                minNeighbors=self.minNeighbors,   
                minSize=(self.minSize, self.minSize),  
                maxSize=(self.maxSize, self.maxSize)
            )


            current_frame_positions = []  # Lista para almacenar posiciones en el frame actual

            # Detectar autos y generar posiciones únicas
            for (x, y, w, h) in cars:

                # Posición central de cada auto
                position = (x + w // 2, y + h // 2)

                # Añade posicion de carro detectado a current_frame_positions
                current_frame_positions.append(position)

                # Dibujar un rectángulo alrededor del auto detectado
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)


            # Actualizar el diccionario de autos detectados en frames anteriores
            new_detected_cars = {}

            for car_id, prev_position in detected_cars.items():

                # Verificar si el auto anterior se encuentra cerca de las posiciones actuales
                for position in current_frame_positions:
                    
                    if abs(prev_position[0] - position[0]) < 50 and abs(prev_position[1] - position[1]) < 50:
                        new_detected_cars[car_id] = position
                        current_frame_positions.remove(position)  # Remover la posición ya asignada
                        break
                else:

                    # Si el auto ha cruzado la línea de salida
                    if prev_position[1] > self.salida_y:
                        # Incrementar el contador de autos salientes
                        self.no_carros += 1  

            # Agregar los autos nuevos a la lista de rastreados
            for position in current_frame_positions:
                new_detected_cars[len(new_detected_cars)] = position

            detected_cars = new_detected_cars

            # Dibujar la línea de salida
            cv2.line(frame, (0, self.salida_y), (frame.shape[1], self.salida_y), (0, 0, 255), 2)

            # Mostrar el contador de autos detectados que salieron en la ventana
            cv2.putText(frame, f'Cars Exited: {self.no_carros}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

            cv2.imshow('Car Detection', frame)

            # Cierra la fincion si se selecciona las teclas (1, q)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()
        return 0

    def toDict(self):
        return {
            'tiempo_verde': self.tVerde,
            'tiempo_rojo': self.tRojo,
            'no_carros': self.no_carros,
        }

    def exportaJson(self):

        file_path = f'outputs/semaforo{self.idSemaforo}.json'
    
        # Check if the directory exists; if not, create it
        directory_path = os.path.dirname(file_path)
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)
        
        # Create or overwrite the file
        data = {"message": "Archivo creado o sobrescrito"}  # Example content
        with open(file_path, 'w') as file:
            json.dump(self.toDict(), file, indent=4)  # Write JSON content to the file
    
    def ajustarTimpo(self, tVerde, tRojo):
        self.tVerde = tVerde
        self.tRojo = tRojo

        conexion = Conexion(driver=self.dbDriver, server=self.dbServer, database=self.dbDatabase)
        conexion.establecerConexion()
        conexion.actualizar("Semaforo", {"tVerde": self.tVerde, "tRojo": self.tRojo}, "id = " + str(self.idSemaforo))
        conexion.cerrarConexion()

        return tVerde+tRojo