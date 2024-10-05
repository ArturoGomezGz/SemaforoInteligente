import cv2
import time
import json


def detect_cars_from_camera(cascade_path):
    car_cascade = cv2.CascadeClassifier(cascade_path)
    cap = cv2.VideoCapture(0)  # Abrir la cámara (usualmente es el índice 0)

    total_cars_detected = 0  # Contador de autos que salen de la imagen
    detected_cars = {}  # Diccionario para almacenar las posiciones de autos rastreados (id: posición)

    exit_line_y = 200  # Coordenada Y para la línea de salida (ajusta según la resolución de la cámara)

    # Obtener el tiempo de inicio
    start_time = time.time()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detección de autos en el frame actual
        cars = car_cascade.detectMultiScale(
            gray,
            scaleFactor=3,
            minNeighbors=30,
            minSize=(70, 70)
        )

        current_frame_positions = []  # Lista para almacenar posiciones en el frame actual

        # Detectar autos y generar posiciones únicas
        for (x, y, w, h) in cars:
            position = (x + w // 2, y + h // 2)  # Posición central de cada auto
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
                    total_cars_detected += 1  # Incrementar el contador de autos salientes

        # Agregar los autos nuevos a la lista de rastreados
        for position in current_frame_positions:
            new_detected_cars[len(new_detected_cars)] = position

        detected_cars = new_detected_cars

        # Dibujar la línea de salida
        cv2.line(frame, (0, exit_line_y), (frame.shape[1], exit_line_y), (0, 0, 255), 2)

        # Mostrar el contador de autos detectados que salieron en la ventana
        cv2.putText(frame, f'Cars Exited: {total_cars_detected}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

        cv2.imshow('Car Detection from Camera', frame)

        # Finalizar después de 60 segundos o si se presiona 'q'
        if time.time() - start_time > 60 or cv2.waitKey(1) & 0xFF == ord('q'):
            break

    print(f"Total cars exited: {total_cars_detected}")  # Imprimir el total al final
    cap.release()
    cv2.destroyAllWindows()

# Llamar a la función con el clasificador de autos
detect_cars_from_camera("../classifier/cascade.xml")
