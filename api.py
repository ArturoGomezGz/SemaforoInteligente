from conexion.conexion import Conexion
from flask import Flask, request, jsonify

app = Flask(__name__)

baseDeDatos = {
    "server" : "localhost",  # Cambia esto a tu servidor SQL
    "database" : "SemaforoInteligente",  # Cambia esto a tu base de datos
    "usuario" : "arturo",
    "contrasena" : "Pword1",
}

@app.route('/semaforos', methods=['GET'])
def get_all_semaforos():
    conexion = Conexion(baseDeDatos)  # Assuming you have a JSON config file
    result = conexion.getSemaforos()
    conexion.cerrarConexion()
    return jsonify(result)

@app.route('/semaforo/<int:semaforo_id>', methods=['GET'])
def get_semaforo(semaforo_id):
    conexion = Conexion(baseDeDatos)
    result = conexion.getSemaforo(semaforo_id)
    conexion.cerrarConexion()
    return jsonify(result)

# ... (similarly for other endpoints)

@app.route('/ajustar_tiempo_semaforo/<int:semaforo_id>', methods=['PUT'])
def ajustar_tiempo_semaforo(semaforo_id):
    t_verde = request.json['tVerde']
    t_rojo = request.json['tRojo']
    conexion = Conexion(baseDeDatos)
    conexion.ajustarTiempoSemaforo(semaforo_id, t_verde, t_rojo)
    conexion.cerrarConexion()
    return jsonify({'message': 'Tiempo de semáforo ajustado correctamente'})

# ... (similarly for other endpoints)

if __name__ == '__main__':
    app.run(debug=True)