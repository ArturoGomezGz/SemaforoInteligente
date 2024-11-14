import pymysql

# Establishing the connection
conexion = pymysql.connect(
    user="arturo",
    password="Pword1",
    host="10.43.125.45",
    database="SemaforoInteligente",
    port=3306
)

# Creating a cursor object
cursor = conexion.cursor()

# Executing the query
cursor.execute("SELECT * FROM usuario")

# Fetching and printing the tables
tables = cursor.fetchall()
print("Tables in the database:")
for table in tables:
    print(table[0])

# Closing the cursor and connection
cursor.close()
conexion.close()
