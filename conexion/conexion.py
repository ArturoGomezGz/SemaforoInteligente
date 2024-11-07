import mysql.connector
import pandas as pd
import json

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
        
        # Convierte la lista de diccionarios a JSON
        json_result = json.dumps(rows, indent=4)
        
        return json_result

    def sQuery(self, query):
        cursor = self.conexion.cursor()
        cursor.execute(query)
        
        # Obtener resultados y nombres de columnas
        resultados = cursor.fetchall()
        columnas = [column[0] for column in cursor.description]
        
        # Llama a la función de transformación a JSON
        json_result = self.query_results_to_json(resultados, columnas)
        
        return json_result

    # GET
    def getSemaforos(self):
        return self.sQuery("SELECT * FROM Semaforo")
    
    def getSemaforo(self, semaforoId):
        return self.sQuery(f"SELECT * FROM Semaforo WHERE id = {semaforoId}")
    
    def getIntersecciones(self):
        return self.sQuery("SELECT * FROM Interseccion")
    
    def getInterseccion(self, interseccionId):
        return self.sQuery(f"SELECT * FROM Interseccion WHERE id = {interseccionId}")

    def getMCiclos(self):
        return self.sQuery("SELECT * FROM mCiclo")
    
    def getMCiclo(self, mCicloId):
        return self.sQuery(f"SELECT * FROM mCiclo WHERE id = {mCicloId}")
    
    def getDCiclos(self):
        return self.sQuery("SELECT * FROM dCiclo")
    
    def getDCiclo(self, dCicloId):
        return self.sQuery(f"SELECT * FROM dCiclo WHERE id = {dCicloId}")
    
    #UPDATE
    def ajustarTiempoSemaforo(self, idSemaforo, tVerde, tRojo):
        self.sQuery(f"UPDATE Semaforo SET tVerde = {tVerde}, tRojo {tRojo} WHERE id = {idSemaforo}")
    
    #POST
    def agregarMCiclo(self, idInterseccion, dia, hora):
        # Convierte los valores en tipos adecuados y asegúrate de que no haya errores de sintaxis
        query = f"INSERT INTO mCiclo (idInterseccion, dia, hora) VALUES ({idInterseccion}, '{dia}', '{hora}')"
        print(query)  # Utiliza esto para ver la consulta generada antes de ejecutarla
        self.sQuery(query)




    def agregarDCiclo(self, idMCiclo, idSemaforo, noCarros):
        self.sQuery(f"INSERT INTO dCiclo (idCiclo, idSemaforo, noCarros) VALUES ({idMCiclo},{idSemaforo},{noCarros})")