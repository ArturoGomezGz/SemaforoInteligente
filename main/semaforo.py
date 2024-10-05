import cv2
import json

class Semaforo:
    def __init__(self, tiempo, no_carros, ruta_video = "", ruta_cascade = "../classifier/cascade.xml", salida_y = 200):
        self.tiempo = tiempo
        self.no_carros = no_carros
        self.ruta_video = ruta_video
        self.ruta_cascade = ruta_cascade
        self.salida_y = salida_y
    
    def __init__(self):
        self.tiempo = 0
        self.no_carros = 0
        self.ruta_video = ""
        self.ruta_cascade = "../classifier/cascade.xml"
        self.salida_y = 200
    
    def imprime(self):
        print(f"Numero de carros: {self.no_carros}")
        print(f"Tiempo en alto: {self.tiempo}")

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
                gray,  # Imagen en escala de grises donde se realizará la detección
                scaleFactor=4,  # Reduce la imagen en un 10% en cada escala; ajustar para más o menos detecciones
                minNeighbors=50,   # Número mínimo de vecinos para considerar una detección válida; ajustar según la precisión deseada
                minSize=(50, 50),  # Tamaño mínimo de los objetos a detectar; ajustar según el tamaño esperado de los coches
                maxSize=(100, 100),  # Tamaño máximo de los objetos a detectar; establecer si quieres limitar el tamaño máximo
                # flags=cv2.CASCADE_SCALE_IMAGE  # Opcional: Usar esta bandera para escalar la imagen en cada escala
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
            'tiempo': self.tiempo,
            'no_carros': self.no_carros,
        }

    def exportaJson(self):
        with open('../outputs/car_count.json', 'w') as file:
            json.dump(self.toDict(), file, indent=4)  # Cambiar a json.dump()