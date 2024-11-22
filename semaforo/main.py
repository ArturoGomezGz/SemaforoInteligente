import RPi.GPIO as GPIO
import time

# Configuración de pines GPIO
LED_PINS = [17, 18, 27, 22, 23, 24]

def setup():
    GPIO.setmode(GPIO.BCM)  # Usa numeración BCM
    for pin in LED_PINS:
        GPIO.setup(pin, GPIO.OUT)  # Configura cada pin como salida
        GPIO.output(pin, GPIO.LOW)  # Asegúrate de que los LEDs estén apagados

def toggle_leds():
    try:
        while True:
            print("Encendiendo LEDs...")
            for pin in LED_PINS:
                GPIO.output(pin, GPIO.HIGH)  # Enciende el LED
                time.sleep(0.5)  # Pausa de 0.5 segundos

            print("Apagando LEDs...")
            for pin in LED_PINS:
                GPIO.output(pin, GPIO.LOW)  # Apaga el LED
                time.sleep(0.5)  # Pausa de 0.5 segundos
    except KeyboardInterrupt:
        print("Saliendo del programa...")
    finally:
        GPIO.cleanup()  # Limpia la configuración GPIO

if __name__ == "__main__":
    setup()
    toggle_leds()
