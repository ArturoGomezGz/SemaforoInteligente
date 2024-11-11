from moviepy.editor import VideoFileClip

def recortar_video(ruta_entrada, ruta_salida, inicio, fin):
    # Cargar el video desde la ruta de entrada
    video = VideoFileClip(ruta_entrada)
    
    # Recortar el video usando el tiempo de inicio y fin
    video_recortado = video.subclip(inicio, fin)
    
    # Guardar el video recortado en la ruta de salida
    video_recortado.write_videofile(ruta_salida, codec="libx264")

# Ejemplo de uso
ruta_entrada = "ruta/del/video/original.mp4"  # Ruta del video original
ruta_salida = "ruta/del/video/recortado.mp4"  # Ruta para guardar el video recortado
inicio = 10  # Tiempo de inicio en segundos
fin = 20     # Tiempo de fin en segundos

recortar_video(ruta_entrada, ruta_salida, inicio, fin)
