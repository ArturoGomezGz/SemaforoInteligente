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

        self.idInterseccion = jsonInterseccion["id"]
        self.no_semaforos = jsonInterseccion["noSemaforos"]
        self.tCiclo = jsonInterseccion["tCiclo"]

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
        carros_acum_s1 = json.loads(conection.getUltimoRegistro(1))[0]["noCarros"]
        carros_acum_s2 = json.loads(conection.getUltimoRegistro(2))[0]["noCarros"]
        conection.cerrarConexion()
        total_carros = carros_acum_s1 + carros_acum_s2
        
        # Verificar si hay carros acumulados
        if total_carros == 0:
            print("carros = 0")
            tiempo_verde = self.tCiclo/self.no_semaforos
            tiempo_rojo = self.tCiclo/self.no_semaforos
        else:
            
            proporcion =  carros_acum_s1 / total_carros

            tiempo_verde = round(proporcion * self.tCiclo)
            tiempo_rojo = self.tCiclo - tiempo_verde

        
        self.semaforos[0].ajustarTimpo(tiempo_verde, tiempo_rojo)
        self.semaforos[1].ajustarTimpo(tiempo_rojo, tiempo_verde)

        print("Datos guardados en la base de datos")
