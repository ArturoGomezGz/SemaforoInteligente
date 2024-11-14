import pymysql

# Establishing the connection
with open('../dbData.json', 'r') as archivo:
    baseDeDatos = json.load(archivo)

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
