import json
from moviepy.video.io.VideoFileClip import VideoFileClip
import os
import random

class Semaforo:
    def __init__(self, id,  tVerde, tRojo, inputSrc, outputSrc):
        self.id = id
        self.tVerde = tVerde
        self.tRojo = tRojo
        self.inputSrc = os.path.join("..", "simulacion", inputSrc)
        self.outputSrc = os.path.join("..", "procesamiento", outputSrc)

    def randNum(self, min, max):
        return str(random.randint(min, max))
    
    def randInput(self):
        self.inputSrc = "resources/video"+self.randNum(1,2)+".mp4"

    def print(self):
        print(f"Semaforo {self.id}, tVerde: {self.tVerde}, tRojo: {self.tRojo}")
        print(f"input: {self.inputSrc}, output: {self.outputSrc}")

    def recortarVideo(self):
        # Cargar el video
        with VideoFileClip(self.inputSrc) as video:
            # Recortar el video desde start_time hasta end_time
            video_recortado = video.subclip(0, self.tRojo)
            
            # Guardar el video recortado
            video_recortado.write_videofile(self.outputSrc, codec="libx264")
            print(f"Video guardado en: {self.outputSrc}")