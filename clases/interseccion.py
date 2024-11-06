import json
from conexion.conexion import Conexion
from datetime import datetime, date, time

class Interseccion:
    def __init__(self, jsonInterseccion, semaforos = None, jsonBaseDeDatos = {}):
        # Datos necesarios para la conexion a la db
        self.baseDeDatos = jsonBaseDeDatos
        self.dbDriver = jsonBaseDeDatos["driver"]
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
        datos = {
            'idInterseccion': self.idInterseccion,
            'dia': str(date.today()),
            'hora': str(datetime.now().time())
        }
        conection.crear("mCiclo", datos)
        noCiclo = conection.leerAll('mCiclo')[-1][0]
        conection.cerrarConexion()
        for i in self.semaforos:
            i.detecta_carros(idCiclo = noCiclo)

    def ajustarTiempo(self):
        conection = Conexion(self.baseDeDatos)
        conection.establecerConexion()
        carros_acum_s1 = conection.leerSpecialQuery("SELECT TOP 2 * FROM dCiclo ORDER BY idCiclo DESC")["noCarros"]
        carros_acum_s2 = conection.leerSpecialQuery("SELECT TOP 2 * FROM dCiclo ORDER BY idCiclo DESC")["noCarros"]
        conection.cerrarConexion()
        total_carros = carros_acum_s1 + carros_acum_s2
        
        # Verificar si hay carros acumulados
        if total_carros == 0:
            tiempo_verde = self.tCiclo/self.no_semaforos
            tiempo_rojo = self.tCiclo/self.no_semaforos
        else:
            
            proporcion =  carros_acum_s1 / total_carros

            tiempo_verde = round(proporcion * self.tCiclo)
            tiempo_rojo = self.tCiclo - tiempo_verde

        self.semaforos[0].ajustarTimpo(tiempo_verde, tiempo_rojo)
        self.semaforos[1].ajustarTimpo(tiempo_rojo, tiempo_verde)

        print("Datos guardados en la base de datos")