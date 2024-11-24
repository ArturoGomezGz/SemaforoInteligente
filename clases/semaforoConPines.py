from clases.semaforo import Semaforo
import RPi.GPIO as GPIO

class SemaforoConPines(Semaforo):
    def __init__(self, jsonSemaforo, pines):
        # Llamamos al constructor de la clase base (Semaforo)
        super().__init__(jsonSemaforo)
        
        # Asignamos los pines proporcionados
        self.redPin = pines["redPin"]
        self.greenPin = pines["greenPin"]
        self.yellowPin = pines["yellowPin"]
        
        # Configuración de los pines GPIO
        GPIO.setmode(GPIO.BCM)  # Usamos el modo de numeración BCM
        GPIO.setup(self.redPin, GPIO.OUT)   # Configura el pin de la luz roja como salida
        GPIO.setup(self.greenPin, GPIO.OUT) # Configura el pin de la luz verde como salida
        GPIO.setup(self.yellowPin, GPIO.OUT) # Configura el pin de la luz amarilla como salida

    def encender_rojo(self):
        GPIO.output(self.redPin, GPIO.HIGH)   # Enciende la luz roja
        GPIO.output(self.greenPin, GPIO.LOW)  # Apaga la luz verde
        GPIO.output(self.yellowPin, GPIO.LOW) # Apaga la luz amarilla

    def encender_verde(self):
        GPIO.output(self.redPin, GPIO.LOW)   # Apaga la luz roja
        GPIO.output(self.greenPin, GPIO.HIGH) # Enciende la luz verde
        GPIO.output(self.yellowPin, GPIO.LOW) # Apaga la luz amarilla

    def encender_amarillo(self):
        GPIO.output(self.redPin, GPIO.LOW)   # Apaga la luz roja
        GPIO.output(self.greenPin, GPIO.LOW)  # Apaga la luz verde
        GPIO.output(self.yellowPin, GPIO.HIGH) # Enciende la luz amarilla

    def apagar_todas(self):
        GPIO.output(self.redPin, GPIO.LOW)   # Apaga la luz roja
        GPIO.output(self.greenPin, GPIO.LOW)  # Apaga la luz verde
        GPIO.output(self.yellowPin, GPIO.LOW) # Apaga la luz amarilla