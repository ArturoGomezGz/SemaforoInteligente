from conexion.conexion import Conexion

# Configura los parámetros de conexión
driver = "SQL Server"
server = "DESKTOP-GI8HMHT"  # Cambia esto a tu servidor SQL
database = "SemaforoInteligente"  # Cambia esto a tu base de datos

# Instancia de la clase Conexion
conexion = Conexion(driver=driver, server=server, database=database)
conexion.establecerConexion()

# Actualizar registro en la tabla Semaforo
# Cambiamos el valor de tVerde a 50 para el registro con id = 1
conexion.actualizar("Semaforo", {"tVerde": 60, "tRojo": 15}, "id = 1")

# Leer registros después de la actualización
resultados = conexion.leer("Semaforo")[0]
print(resultados)

# Cerrar la conexión
conexion.cerrarConexion()
