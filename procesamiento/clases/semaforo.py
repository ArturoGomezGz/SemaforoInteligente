import cv2
import json
import os
import requests
#from conexion.conexion import Conexion

class Semaforo:
    def __init__(self, jsonSemaforo):
        self.idSemaforo = jsonSemaforo["id"]
        self.tVerde = jsonSemaforo["tVerde"] # Tiempo (en segundos) en verde (ulitmos 5 segundo son amarillo)
        self.tRojo = jsonSemaforo["tRojo"] # Tiempo en rojo (en segundos)
        self.ruta_video = jsonSemaforo["rutaVideo"] # Ruta del video para el conteo de carros
        self.ruta_cascade = jsonSemaforo["rutaCascade"] # Ruta del archivo cascade (modelo de vision artificial)
        self.salida_y = jsonSemaforo["salidaY"] # Numero de pixeles desde arriba (en y) para contar carros
        self.scaleFactor = jsonSemaforo["scaleFactor"]  # Reduce la imagen en un 10% en cada escala; ajustar para más o menos detecciones
        self.minNeighbors = jsonSemaforo["minNeighbors"]   # Número mínimo de vecinos para considerar una detección válida; ajustar según la precisión deseada
        self.minSize = jsonSemaforo["minSize"]  # Tamaño mínimo de los objetos a detectar; ajustar según el tamaño esperado de los coches
        self.maxSize = jsonSemaforo["maxSize"]  # Tamaño máximo de los objetos a detectar; establecer si quieres limitar el tamaño máximo
    
    def cargarPorSql():
        return 1

    def imprime(self):
        print(f"Tiempo en verde: {self.tVerde}")
        print(f"Tiempo en alto: {self.tRojo}")

    def detecta_carros(self, idCiclo):
        print("Detección comenzada")
        noCarros = 0
        car_cascade = cv2.CascadeClassifier(self.ruta_cascade)
        cap = cv2.VideoCapture(self.ruta_video)

        detected_cars = {}  # Diccionario para almacenar las posiciones de autos rastreados (id: posición)

        # Bucle while que itera frame por frame 
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Detección de autos en el frame actual
            cars = car_cascade.detectMultiScale(
                gray,
                scaleFactor=float(self.scaleFactor),
                minNeighbors=int(self.minNeighbors),
                minSize=(int(self.minSize), int(self.minSize)),
                maxSize=(int(self.maxSize), int(self.maxSize))
            )

            current_frame_positions = []  # Lista para almacenar posiciones en el frame actual

            # Detectar autos y generar posiciones únicas
            for (x, y, w, h) in cars:
                # Posición central de cada auto
                position = (x + w // 2, y + h // 2)

                # Añade posición de carro detectado a current_frame_positions
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
                    if prev_position[1] > int(self.salida_y):
                        # Incrementar el contador de autos salientes
                        noCarros += 1

            # Agregar los autos nuevos a la lista de rastreados
            for position in current_frame_positions:
                new_detected_cars[len(new_detected_cars)] = position

            detected_cars = new_detected_cars

            # Dibujar la línea de salida
            cv2.line(frame, (0, int(self.salida_y)), (frame.shape[1], int(self.salida_y)), (0, 0, 255), 2)

            # Mostrar el contador de autos detectados que salieron en la ventana
            cv2.putText(frame, f'Cars Exited: {noCarros}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

            cv2.imshow('Car Detection', frame)

            # Cierra la función si se seleccionan las teclas (1, q)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()
        print("Detección terminada")

        # Usar la API para registrar el dCiclo
        url = "http://127.0.0.1:5000/addDCiclo"  # Cambia el host/puerto si es necesario
        data = {
            "idMCiclo": idCiclo,
            "idSemaforo": self.idSemaforo,
            "noCarros": noCarros
        }

        try:
            response = requests.post(url, json=data)
            if response.status_code == 201:
                print("dCiclo registrado correctamente en la API")
            else:
                print(f"Error al registrar dCiclo: {response.status_code} - {response.json()}")
        except requests.exceptions.RequestException as e:
            print(f"Error al conectar con la API: {e}")

        return 0

    def ajustarTimpo(self, tVerde, tRojo):
        self.tVerde = tVerde
        self.tRojo = tRojo

        # URL de la API (ajusta según el host y el puerto en el que esté corriendo tu API)
        url = f"http://127.0.0.1:5000/adjustTime/{self.idSemaforo}"

        # Datos para enviar en la solicitud PUT
        data = {
            "tVerde": self.tVerde,
            "tRojo": self.tRojo
        }

        try:
            # Realizar la solicitud PUT
            response = requests.put(url, json=data)

            # Comprobar el código de estado de la respuesta
            if response.status_code == 200:
                print("Tiempos de semáforo actualizados correctamente.")
            else:
                print(f"Error al actualizar tiempos: {response.status_code} - {response.json()}")
        except requests.exceptions.RequestException as e:
            print(f"Error de conexión al realizar la solicitud: {e}")

        return tVerde + tRojo
