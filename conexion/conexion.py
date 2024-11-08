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
        rows = [{col: str(value) for col, value in zip(columnas, row)} for row in resultados]
        
        # Convierte la lista de diccionarios a JSON
        json_result = json.dumps(rows, indent=4)
        
        return json_result

    def sQuery(self, query):
        cursor = self.conexion.cursor()
        cursor.execute(query)
        self.conexion.commit()

    def sQueryGET(self, query):
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
    
    def getUltimoRegistro(self, idSemaforo):
        return self.sQueryGET(f"SELECT * FROM dCiclo WHERE idSemaforo = {idSemaforo} ORDER BY idCiclo DESC LIMIT 1")

    #UPDATE
    def ajustarTiempoSemaforo(self, idSemaforo, tVerde, tRojo):
        print(f"UPDATE Semaforo SET tVerde = {tVerde}, tRojo {tRojo} WHERE id = {idSemaforo}")
        self.sQuery(f"UPDATE Semaforo SET tVerde = {tVerde}, tRojo {tRojo} WHERE id = {idSemaforo}")
    
    #POST
    def agregarMCiclo(self, idInterseccion, dia, hora):
        self.sQuery(f"INSERT INTO mCiclo (idInterseccion, dia, hora) VALUES ({idInterseccion},'{dia}','{hora}')")    

    def agregarDCiclo(self, idMCiclo, idSemaforo, noCarros):
        self.sQuery(f"INSERT INTO dCiclo (idCiclo, idSemaforo, noCarros) VALUES ({idMCiclo},{idSemaforo},{noCarros})")

    def limpiarRegistros(self):
        self.sQuery("DELETE FROM dCiclo")
        self.sQuery("ALTER TABLE dCiclo AUTO_INCREMENT = 1")
        self.sQuery("DELETE FROM mCiclo")
        self.sQuery("ALTER TABLE mCiclo AUTO_INCREMENT = 1")