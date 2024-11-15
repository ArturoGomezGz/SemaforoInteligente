import pymysql
import json
from flask import Flask, request, jsonify


class Conexion:
    def __init__(self, jsonBaseDeDatos):
        self.dbServer = jsonBaseDeDatos["server"]
        self.dbDatabase = jsonBaseDeDatos["database"]
        self.dbUsuario = jsonBaseDeDatos["usuario"]
        self.dbContrasena = jsonBaseDeDatos["contrasena"]
        self.dbPort = jsonBaseDeDatos["port"]
        self.conexion = pymysql.connect(
            host=self.dbServer,
            user=self.dbUsuario,
            password=self.dbContrasena,
            database=self.dbDatabase,
            port=self.dbPort
        )

    def cerrarConexion(self):
        """Cierra la conexión y el cursor."""
        if self.conexion:
            self.conexion.close()
            print("Conexión cerrada exitosamente.")

    def query_results_to_json(self, resultados, columnas):
        # Convierte cada fila en un diccionario usando las columnas proporcionadas
        rows = [{col: str(value) for col, value in zip(columnas, row)} for row in resultados]
        
        # Convierte la lista de diccionarios a JSON
        json_result = json.dumps(rows, indent=4)
        
        return json_result

    def sQuery(self, query):
        with self.conexion.cursor() as cursor:
            cursor.execute(query)
            self.conexion.commit()

    def sQueryGET(self, query):
        with self.conexion.cursor() as cursor:
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

    def getUsuario(self, usuario):
        return self.sQueryGET(f"SELECT * FROM usuario WHERE usuario = '{usuario}'")
    
    def getSumByRange(self, idInterseccion, timeIni, timeFin, date):
        return self.sQueryGET(f"""
            SELECT 
                idSemaforo,
                SUM(noCarros) AS noCarros
            FROM dCiclo 
            JOIN mCiclo ON mCiclo.id = dCiclo.idCiclo
            WHERE mCiclo.dia = '{date}'
            AND mCiclo.hora >= '{timeIni}' AND mCiclo.hora < '{timeFin}'
            AND idInterseccion = {idInterseccion}
            GROUP BY idSemaforo
            """)

    def getCiclosRangeSemaforo(self, idSemaforo, timeIni, timeFin, date):
        return self.sQueryGET(f"""
            SELECT 
                noCarros,
                hora
            FROM mCiclo
            JOIN dCiclo ON mCiclo.id = dCiclo.idCiclo
            WHERE dCiclo.idSemaforo = {idSemaforo}
            AND dia = '{date}' 
            AND hora > '{timeIni}' 
            AND hora < '{timeFin}';
            """)


    # UPDATE
    def ajustarTiempoSemaforo(self, idSemaforo, tVerde, tRojo):
        self.sQuery(f"UPDATE Semaforo SET tVerde = {tVerde}, tRojo = {tRojo} WHERE id = {idSemaforo}")
    
    # POST
    def agregarMCiclo(self, idInterseccion, dia, hora):
        self.sQuery(f"INSERT INTO mCiclo (idInterseccion, dia, hora) VALUES ({idInterseccion},'{dia}','{hora}')")    

    def agregarDCiclo(self, idMCiclo, idSemaforo, noCarros):
        self.sQuery(f"INSERT INTO dCiclo (idCiclo, idSemaforo, noCarros) VALUES ({idMCiclo},{idSemaforo},{noCarros})")

    def limpiarRegistros(self):
        self.sQuery("DELETE FROM dCiclo")
        self.sQuery("ALTER TABLE dCiclo AUTO_INCREMENT = 1")
        self.sQuery("DELETE FROM mCiclo")
        self.sQuery("ALTER TABLE mCiclo AUTO_INCREMENT = 1")
    
    # PUT
    def updateInterseccionTime(self, idInterseccion, tCiclo):
        self.sQuery(f"UPDATE Interseccion SET tCiclo = {tCiclo} WHERE id = {idInterseccion}")

    def createUsuario(self, usuario, contrasena, nombre):
        self.sQuery(f"INSERT INTO usuario (usuario, contrasena, nombre) VALUES ('{usuario}', '{contrasena}', '{nombre}')")
