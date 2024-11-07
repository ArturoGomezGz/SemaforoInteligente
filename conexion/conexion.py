import mysql.connector
import pandas as pd
import json
from datetime import date

class Conexion:
    def __init__(self, jsonBaseDeDatos):
        self.dbServer = jsonBaseDeDatos["server"]
        self.dbDatabase = jsonBaseDeDatos["database"]
        self.dbUsuario = jsonBaseDeDatos["usuario"]
        self.dbContrasena = jsonBaseDeDatos["contrasena"]
        self.conexion = mysql.connector.connect(
            host=self.dbServer,
            user=self.dbUsuario,
            passwd=self.dbContrasena,
            database=self.dbDatabase
        )

    def cerrarConexion(self):
        """Cierra la conexión y el cursor."""
        if self.conexion:
            self.conexion.close()
            self.cursor = None
            print("Conexión cerrada exitosamente.")

    def query_results_to_json(self, resultados, columnas):
        # Convierte cada fila en un diccionario usando las columnas proporcionadas
        rows = [dict(zip(columnas, row)) for row in resultados]

        # Función para convertir tipos no serializables (como date) a algo que JSON pueda manejar
        def default_converter(o):
            if isinstance(o, date):
                return o.isoformat()  # Convierte el objeto date a una cadena en formato ISO
            raise TypeError(f"Object of type {o.__class__.__name__} is not JSON serializable")
        
        # Convierte la lista de diccionarios a JSON, usando el convertidor personalizado
        json_result = json.dumps(rows, indent=4, default=default_converter)
        
        return json_result


    def sQueryGET(self, query):
        cursor = self.conexion.cursor()
        cursor.execute(query)
        
        # Obtener resultados y nombres de columnas
        resultados = cursor.fetchall()
        columnas = [column[0] for column in cursor.description]
        
        # Llama a la función de transformación a JSON
        json_result = self.query_results_to_json(resultados, columnas)
        
        return json_result

    def sQueryPOST(self, query):
        cursor = self.conexion.cursor()
        cursor.execute(query)
    
    # GET
    def getSemaforos(self):
        return self.sQueryGET("SELECT * FROM Semaforo")
    
    def getSemaforo(self, semaforoId):
        return self.sQueryGET(f"SELECT * FROM Semaforo WHERE id = {semaforoId}")
    
    def getIntersecciones(self):
        return self.sQueryGET("SELECT * FROM Interseccion")
    
    def getInterseccion(self, interseccionId):
        return self.sQueryGET(f"SELECT * FROM Interseccion WHERE id = {interseccionId}")

    def getMCiclos(self):
        return self.sQueryGET("SELECT * FROM mCiclo")
    
    def getMCiclo(self, mCicloId):
        return self.sQueryGET(f"SELECT * FROM mCiclo WHERE id = {mCicloId}")
    
    def getDCiclos(self):
        return self.sQueryGET("SELECT * FROM dCiclo")
    
    def getDCiclo(self, dCicloId):
        return self.sQueryGET(f"SELECT * FROM dCiclo WHERE id = {dCicloId}")
    
    #UPDATE
    def ajustarTiempoSemaforo(self, idSemaforo, tVerde, tRojo):
        self.sQueryGET(f"UPDATE Semaforo SET tVerde = {tVerde}, tRojo {tRojo} WHERE id = {idSemaforo}")
    
    #POST
    def agregarMCiclo(self, idInterseccion, dia, hora):
        query = f"INSERT INTO mCiclo (idInterseccion, dia, hora) VALUES ({idInterseccion}, '{dia}', '{hora}')"
        self.sQueryPOST(query)

    def agregarDCiclo(self, idMCiclo, idSemaforo, noCarros):
        self.sQueryPOST(f"INSERT INTO dCiclo (idCiclo, idSemaforo, noCarros) VALUES ({idMCiclo},{idSemaforo},{noCarros})")