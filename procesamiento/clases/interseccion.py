import json
from conexion.conexion import Conexion
from datetime import datetime, date, time

class Interseccion:
    def __init__(self, jsonInterseccion, semaforos = None, jsonBaseDeDatos = {}):
        # Datos necesarios para la conexion a la db
        self.baseDeDatos = jsonBaseDeDatos
        self.dbServer = jsonBaseDeDatos["server"]
        self.dbDatabase = jsonBaseDeDatos["database"]
        self.dbUsuario = jsonBaseDeDatos["usuario"]
        self.dbContrasena = jsonBaseDeDatos["contrasena"]

        if semaforos is None:
            semaforos = []
        self.semaforos = semaforos

        self.idInterseccion = int(jsonInterseccion["id"])
        self.no_semaforos = int(jsonInterseccion["noSemaforos"])
        self.tCiclo = int(jsonInterseccion["tCiclo"])

    def procesar(self):
        conection = Conexion(self.baseDeDatos)
        dia = str(date.today())
        hora = str(datetime.now().time())
        conection.agregarMCiclo(self.idInterseccion, dia, hora)
        print("mCiclo registrado")
        jsonNoCiclo = conection.getMCiclos()
        noCiclo = json.loads(jsonNoCiclo)[-1]['id']
        conection.cerrarConexion()
        for i in self.semaforos:
            i.detecta_carros(noCiclo)

    def ajustarTiempo(self):
        conection = Conexion(self.baseDeDatos)
        carros_acum_s1 = int(json.loads(conection.getUltimoRegistro(1))[0]["noCarros"])
        carros_acum_s2 = int(json.loads(conection.getUltimoRegistro(2))[0]["noCarros"])
        conection.cerrarConexion()
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
        
        # Ajustar los semáforos
        self.semaforos[0].ajustarTimpo(nuevo_tiempo_verde, nuevo_tiempo_rojo)
        self.semaforos[1].ajustarTimpo(nuevo_tiempo_rojo, nuevo_tiempo_verde)
        
        print("Tiempo de semaforo ajustado correctamnete en DB")

