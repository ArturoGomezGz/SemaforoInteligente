from clases.semaforo import Semaforo
from moviepy.editor import VideoFileClip

class SemaforoSimulacion(Semaforo):
    def __init__(self, jsonSemaforo, inputSrc, outputSrc):
        # Llamamos al constructor de la clase base (Semaforo)
        super().__init__(jsonSemaforo)
        
        self.inputSrc = inputSrc
        self.outputSrc = outputSrc

    def randNum(self, min, max):
        return str(random.randint(min, max))
    
    def randInput(self):
        self.inputSrc = "resources/video"+self.randNum(1,2)+".mp4"

    def recortarVideo(self):
        # Cargar el video
        with VideoFileClip(self.inputSrc) as video:
            # Recortar el video desde start_time hasta end_time
            video_recortado = video.subclip(0, self.tRojo)
            
            # Guardar el video recortado
            video_recortado.write_videofile(self.outputSrc, codec="libx264")
            print(f"Video guardado en: {self.outputSrc}")