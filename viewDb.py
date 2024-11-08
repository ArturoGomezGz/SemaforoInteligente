from conexion.conexion import Conexion
import json
import time

baseDeDatos = {
    "server" : "localhost",  # Cambia esto a tu servidor SQL
    "database" : "SemaforoInteligente",  # Cambia esto a tu base de datos
    "usuario" : "arturo",
    "contrasena" : "Pword1",
}

conection = Conexion(baseDeDatos)

while True:
    print("mCiclos --------------------------------------")
    json_data = conection.getMCiclos()
    data = json.loads(json_data)
    for i in data:
        print(i)
    print("")

    print("dCiclos --------------------------------------")
    json_data = conection.getDCiclos()
    data = json.loads(json_data)
    for i in data:
        print(i)
    print("")

    print("Semaforos --------------------------------------")
    json_data = conection.getSemaforos()
    data = json.loads(json_data)
    for i in data:
        print(i)
    print("")

    print("Interseciones --------------------------------------")
    json_data = conection.getIntersecciones()
    data = json.loads(json_data)
    for i in data:
        print(i)
    print("")

    time.sleep(5)

conection.cerrarConexion()




