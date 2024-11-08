from conexion.conexion import Conexion
import json

baseDeDatos = {
    "server" : "localhost",  # Cambia esto a tu servidor SQL
    "database" : "SemaforoInteligente",  # Cambia esto a tu base de datos
    "usuario" : "arturo",
    "contrasena" : "Pword1",
}

conection = Conexion(baseDeDatos)

json_data = conection.getMCiclos()
data = json.loads(json_data)
print(data)

json_data = conection.getDCiclos()
data = json.loads(json_data)
print(data)

json_data = conection.getSemaforos()
data = json.loads(json_data)
print(data)

json_data = conection.getIntersecciones()
data = json.loads(json_data)
print(data)

conection.cerrarConexion()




