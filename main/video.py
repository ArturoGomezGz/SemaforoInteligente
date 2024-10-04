import cv2
import json


# --video_path-- Ruta del video a detectar
# --cascade_path-- Ruta del archivo, cascade.xml (el cerebro del programa)
# --exit_line_y-- Linea en la cual al cruzar se aumenta el numero de carros (pixeles desde arriba)

def detect_cars(video_path, cascade_path, exit_line_y):
    car_cascade = cv2.CascadeClassifier(cascade_path)
    cap = cv2.VideoCapture(video_path)

    total_cars_detected = 0  # Contador de autos que salen de la imagen
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
                if prev_position[1] > exit_line_y:
                    # Incrementar el contador de autos salientes
                    total_cars_detected += 1  

        # Agregar los autos nuevos a la lista de rastreados
        for position in current_frame_positions:
            new_detected_cars[len(new_detected_cars)] = position

        detected_cars = new_detected_cars

        # Dibujar la línea de salida
        cv2.line(frame, (0, exit_line_y), (frame.shape[1], exit_line_y), (0, 0, 255), 2)

        # Mostrar el contador de autos detectados que salieron en la ventana
        cv2.putText(frame, f'Cars Exited: {total_cars_detected}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

        cv2.imshow('Car Detection', frame)

        # Cierra la fincion si se selecciona las teclas (1, q)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break



    print(f"Total cars exited: {total_cars_detected}")  # Imprimir el total al final
    cap.release()
    cv2.destroyAllWindows()

# Llamar a la función con el video y el clasificador de autos
detect_cars("../resources/video2.mp4", "../classifier/cascade.xml", 200)
