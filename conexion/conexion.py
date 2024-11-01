import pyodbc

class Conexion:
    def __init__(self, driver="SQL Server", server="", database="", usuario="", contrasena=""):
        self.driver = driver
        self.server = server
        self.database = database
        self.user = usuario
        self.password = contrasena
        self.stringConexion = f'DRIVER={{{self.driver}}};SERVER={self.server};DATABASE={self.database};Trusted_Connection=yes;'
        self.conexion = None
        self.cursor = None

    def establecerConexion(self):
        """Establece la conexión y el cursor si no están definidos."""
        if self.conexion is None or self.cursor is None:
            self.conexion = pyodbc.connect(self.stringConexion)
            self.cursor = self.conexion.cursor()

    def cerrarConexion(self):
        """Cierra la conexión y el cursor."""
        if self.conexion:
            self.conexion.close()
            self.cursor = None
            print("Conexión cerrada exitosamente.")

    def crear(self, tabla, datos):
        """Inserta datos en una tabla especificada."""
        self.establecerConexion()
        columnas = ', '.join(datos.keys())
        valores = ', '.join(['?'] * len(datos))
        query = f"INSERT INTO {tabla} ({columnas}) VALUES ({valores})"
        self.cursor.execute(query, list(datos.values()))
        self.conexion.commit()
        print("Datos insertados exitosamente.")

    def leer(self, tabla, condiciones=""):
        """Lee datos de una tabla con condiciones opcionales."""
        self.establecerConexion()
        query = f"SELECT * FROM {tabla} {condiciones}"
        self.cursor.execute(query)
        resultados = self.cursor.fetchall()
        return resultados[0] #Devielve uicamente el plrimer dato

    def leerAll(self, tabla):
        """Lee datos de una tabla con condiciones opcionales."""
        self.establecerConexion()
        query = f"SELECT * FROM {tabla}"
        self.cursor.execute(query)
        resultados = self.cursor.fetchall()
        return resultados #Devielve todos los datos

    def actualizar(self, tabla, datos, condiciones):
        """Actualiza datos en una tabla especificada con condiciones."""
        self.establecerConexion()
        set_clause = ', '.join([f"{col} = ?" for col in datos.keys()])
        query = f"UPDATE {tabla} SET {set_clause} WHERE {condiciones}"
        self.cursor.execute(query, list(datos.values()))
        self.conexion.commit()
        print("Datos actualizados exitosamente.")

    def eliminar(self, tabla, condiciones):
        """Elimina datos de una tabla con las condiciones especificadas."""
        self.establecerConexion()
        query = f"DELETE FROM {tabla} WHERE {condiciones}"
        self.cursor.execute(query)
        self.conexion.commit()
        print("Datos eliminados exitosamente.")
