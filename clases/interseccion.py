import json
import requests
#from conexion.conexion import Conexion
from datetime import datetime, date, time

class Interseccion:
    def __init__(self, jsonInterseccion, semaforos = None):
        if semaforos is None:
            semaforos = []
        self.semaforos = semaforos

        self.idInterseccion = int(jsonInterseccion["id"])
        self.no_semaforos = int(jsonInterseccion["noSemaforos"])
        self.tCiclo = int(jsonInterseccion["tCiclo"])

    def procesar(self):
        dia = str(date.today())
        hora = str(datetime.now().time())

        # Registrar un nuevo mCiclo usando la API
        url_agregar_mciclo = "http://127.0.0.1:5000/addMCiclo"
        data_mciclo = {
            "idInterseccion": self.idInterseccion,
            "dia": dia,
            "hora": hora
        }

        try:
            response = requests.post(url_agregar_mciclo, json=data_mciclo)
            if response.status_code == 201:
                print("mCiclo registrado")
            else:
                print(f"Error al registrar mCiclo: {response.status_code} - {response.json()}")
                return
        except requests.exceptions.RequestException as e:
            print(f"Error al conectar con la API: {e}")
            return

        # Obtener el último mCiclo registrado usando la API
        url_get_mciclos = "http://127.0.0.1:5000/mciclos"

        try:
            response = requests.get(url_get_mciclos)
            if response.status_code == 200:
                mciclos = json.loads(response.json())
                noCiclo = mciclos[-1]['id']  # Obtener el último id de mCiclo
            else:
                print(f"Error al obtener mCiclos: {response.status_code} - {response.json()}")
                return
        except requests.exceptions.RequestException as e:
            print(f"Error al conectar con la API: {e}")
            return

        # Procesar los semáforos para detectar autos
        for semaforo in self.semaforos:
            semaforo.detecta_carros(noCiclo)

    def ajustarTiempo(self):
        # URL base de la API
        base_url = "http://127.0.0.1:5000"

        try:
            # Obtener el último registro para el semáforo 1
            response_s1 = requests.get(f"{base_url}/ultimo_registro/1")
            if response_s1.status_code == 200:
                carros_acum_s1 = int(json.loads(response_s1.json())[0]["noCarros"])
            else:
                print(f"Error al obtener el último registro del semáforo 1: {response_s1.status_code} - {response_s1.json()}")
                return

            # Obtener el último registro para el semáforo 2
            response_s2 = requests.get(f"{base_url}/ultimo_registro/2")
            if response_s2.status_code == 200:
                carros_acum_s2 = int(json.loads(response_s2.json())[0]["noCarros"])
            else:
                print(f"Error al obtener el último registro del semáforo 2: {response_s2.status_code} - {response_s2.json()}")
                return

        except requests.exceptions.RequestException as e:
            print(f"Error de conexión con la API: {e}")
            return

        # Calcular el total de carros
        total_carros = carros_acum_s1 + carros_acum_s2

        if total_carros == 0:
            print("carros = 0")
            tiempo_verde = self.tCiclo / self.no_semaforos
            tiempo_rojo = self.tCiclo / self.no_semaforos
        else:
            proporcion = carros_acum_s1 / total_carros
            tiempo_deseado_verde = round(proporcion * self.tCiclo)

            # Ajuste gradual
            MAX_CAMBIO_TIEMPO = 3
            cambio_verde = tiempo_deseado_verde - int(self.semaforos[0].tVerde)
            cambio_verde = max(-MAX_CAMBIO_TIEMPO, min(MAX_CAMBIO_TIEMPO, cambio_verde))

            # Aplicar ajuste gradual
            nuevo_tiempo_verde = int(self.semaforos[0].tVerde) + cambio_verde

            # Límites de tiempo
            TIEMPO_MIN_VERDE = 10
            TIEMPO_MAX_VERDE = self.tCiclo - TIEMPO_MIN_VERDE
            nuevo_tiempo_verde = max(TIEMPO_MIN_VERDE, min(TIEMPO_MAX_VERDE, nuevo_tiempo_verde))

            nuevo_tiempo_rojo = self.tCiclo - nuevo_tiempo_verde

        # Ajustar los semáforos usando la API
        try:
            for semaforo, verde, rojo in zip(
                self.semaforos,
                [nuevo_tiempo_verde, nuevo_tiempo_rojo],
                [nuevo_tiempo_rojo, nuevo_tiempo_verde]
            ):
                url_ajustar_tiempo = f"{base_url}/adjustTime/{semaforo.idSemaforo}"
                data = {"tVerde": verde, "tRojo": rojo}
                response = requests.put(url_ajustar_tiempo, json=data)

                if response.status_code == 200:
                    print(f"Tiempo del semáforo {semaforo.idSemaforo} ajustado correctamente.")
                else:
                    print(f"Error al ajustar el tiempo del semáforo {semaforo.idSemaforo}: {response.status_code} - {response.json()}")

        except requests.exceptions.RequestException as e:
            print(f"Error de conexión con la API al ajustar tiempos: {e}")

        print("Tiempo de semáforo ajustado correctamente en la base de datos.")

    import time

class Interseccion:
    def __init__(self, jsonInterseccion, semaforos=None):
        if semaforos is None:
            semaforos = []
        self.semaforos = semaforos

        self.idInterseccion = int(jsonInterseccion["id"])
        self.no_semaforos = int(jsonInterseccion["noSemaforos"])
        self.tCiclo = int(jsonInterseccion["tCiclo"])

    def ciclo_semaforos(self):
        """
        Controla el ciclo de los semáforos durante el tiempo de ciclo.
        Enciende la luz verde en el semáforo 1 y la luz roja en el semáforo 2,
        luego enciende el amarillo en el semáforo 1 durante los últimos 5 segundos
        del tiempo verde. Después, intercambia el verde entre los semáforos.
        """
        tVerde1 = self.semaforos[0].tVerde
        tRojo2 = self.semaforos[1].tRojo
        tRojo1 = self.semaforos[0].tRojo
        tVerde2 = self.semaforos[1].tVerde

        # Enciende el semáforo 1 en verde y el semáforo 2 en rojo
        self.semaforos[0].encender_verde()
        self.semaforos[1].encender_rojo()
        print(f"Semáforo 1 en verde por {tVerde1} segundos.")
        print(f"Semáforo 2 en rojo por {tRojo2} segundos.")
        
        # Espera durante tVerde1 menos los 5 segundos para encender amarillo
        time.sleep(tVerde1 - 5)
        
        # Los últimos 5 segundos del verde del semáforo 1, enciende el amarillo
        self.semaforos[0].encender_amarillo()
        print("Semáforo 1 en amarillo durante los últimos 5 segundos.")
        
        # Espera 5 segundos con el semáforo 1 en amarillo
        time.sleep(5)

        # Después de eso, apaga el semáforo 1 y enciende el semáforo 2 en verde
        self.semaforos[0].apagar_todas()
        self.semaforos[1].encender_verde()
        print(f"Semáforo 2 en verde por {tVerde2} segundos.")
        
        # Espera el tiempo de tVerde2
        time.sleep(tVerde2)

        # Apagar semáforo 2 y encender semáforo 1 en rojo
        self.semaforos[1].apagar_todas()
        self.semaforos[0].encender_rojo()
        print(f"Semáforo 1 en rojo por {tRojo1} segundos.")
        
        # Espera el tiempo de tRojo1
        time.sleep(tRojo1)
        
        # Se repite el ciclo
        print("Ciclo completado.")
