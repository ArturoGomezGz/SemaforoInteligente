import json

class Interseccion:
    def __init__(self, semaforos = None, tCiclo = 120):
        if semaforos is None:
            semaforos = []
        self.semaforos = semaforos
        self.no_semaforos = len(semaforos)
        self.tCiclo = tCiclo

    def procesar(self):
        for i in self.semaforos:
            i.detecta_carros()
            i.exportaJson()

    def ajustarTiempo(self):
        # Cargar la cantidad de carros acumulados desde los archivos JSON
        carros_acum_s1 = json.load(open('./outputs/semaforo1.json', 'r'))
        carros_acum_s2 = json.load(open('./outputs/semaforo2.json', 'r'))

        # Calcular el total de carros acumulados
        total_carros = carros_acum_s1["no_carros"] + carros_acum_s2["no_carros"]
        

        # Verificar si hay carros acumulados
        if total_carros == 0:
            tiempo_verde = self.tCiclo/self.no_semaforos
            tiempo_rojo = self.tCiclo/self.no_semaforos
        else:
            
            proporcion =  carros_acum_s1["no_carros"] / total_carros

            tiempo_verde = round(proporcion * self.tCiclo)
            tiempo_rojo = self.tCiclo - tiempo_verde

        self.semaforos[0].ajustarTimpo(tiempo_verde, tiempo_rojo)
        self.semaforos[1].ajustarTimpo(tiempo_rojo, tiempo_verde)
        self.semaforos[0].exportaJson()
        self.semaforos[1].exportaJson()

