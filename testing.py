import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="arturo",
    password="Pword1",
    database="SemaforoInteligente"
)

cursor = conexion.cursor()
cursor.execute("SHOW TABLES")
for tabla in cursor:
    print(tabla)

conexion.close()
