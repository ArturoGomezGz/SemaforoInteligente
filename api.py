from conexion.conexion import Conexion
from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

with open('./dbData.json', 'r') as archivo:
    baseDeDatos = json.load(archivo)

@app.route('/semaforos', methods=['GET'])
def get_all_semaforos():
    conexion = Conexion(baseDeDatos)
    result = conexion.getSemaforos()
    conexion.cerrarConexion()
    return jsonify(result)

@app.route('/semaforo/<int:semaforo_id>', methods=['GET'])
def get_semaforo(semaforo_id):
    conexion = Conexion(baseDeDatos)
    result = conexion.getSemaforo(semaforo_id)
    conexion.cerrarConexion()
    return jsonify(result)

@app.route('/intersecciones', methods=['GET'])
def get_all_intersecciones():
    conexion = Conexion(baseDeDatos)
    result = conexion.getIntersecciones()
    conexion.cerrarConexion()
    return jsonify(result)

@app.route('/interseccion/<int:interseccion_id>', methods=['GET'])
def get_interseccion(interseccion_id):
    conexion = Conexion(baseDeDatos)
    result = conexion.getInterseccion(interseccion_id)
    conexion.cerrarConexion()
    return jsonify(result)

@app.route('/mciclos', methods=['GET'])
def get_all_mciclos():
    conexion = Conexion(baseDeDatos)
    result = conexion.getMCiclos()
    conexion.cerrarConexion()
    return jsonify(result)

@app.route('/mciclo/<int:mciclo_id>', methods=['GET'])
def get_mciclo(mciclo_id):
    conexion = Conexion(baseDeDatos)
    result = conexion.getMCiclo(mciclo_id)
    conexion.cerrarConexion()
    return jsonify(result)

@app.route('/dciclos', methods=['GET'])
def get_all_dciclos():
    conexion = Conexion(baseDeDatos)
    result = conexion.getDCiclos()
    conexion.cerrarConexion()
    return jsonify(result)

@app.route('/dciclo/<int:dciclo_id>', methods=['GET'])
def get_dciclo(dciclo_id):
    conexion = Conexion(baseDeDatos)
    result = conexion.getDCiclo(dciclo_id)
    conexion.cerrarConexion()
    return jsonify(result)

@app.route('/carSumRange/<int:idInterseccion>/<string:timeIni>/<string:timeFin>/<string:date>', methods=['GET'])
def get_car_sum(idInterseccion,timeIni, timeFin, date):
    conexion = Conexion(baseDeDatos)
    result = conexion.getSumByRange(idInterseccion,timeIni, timeFin, date)
    conexion.cerrarConexion()
    return jsonify(result)

@app.route('/carSumRangeByCiclos/<int:idSemaforo>/<string:timeIni>/<string:timeFin>/<string:date>', methods=['GET'])
def get_car_sum_ciclos(idSemaforo,timeIni, timeFin, date):
    conexion = Conexion(baseDeDatos)
    result = conexion.getCiclosRangeSemaforo(idSemaforo, timeIni, timeFin, date)
    conexion.cerrarConexion()
    return jsonify(result)

@app.route('/ultimo_registro/<int:semaforo_id>', methods=['GET'])
def get_ultimo_registro(semaforo_id):
    conexion = Conexion(baseDeDatos)
    result = conexion.getUltimoRegistro(semaforo_id)
    conexion.cerrarConexion()
    return jsonify(result)

@app.route('/updateTCiclo', methods=['PUT'])
def updateTCiclo():
    # Obtener los datos JSON del cuerpo de la solicitud
    data = request.json
    interseccion_id = data.get("interseccion")
    tCiclo = data.get("tiempoCiclo")

    # Asegúrate de que se proporcionan todos los campos
    if interseccion_id is None or tCiclo is None:
        return jsonify({"error": "Todos los campos son requeridos"}), 400

    # Conectar a la base de datos y actualizar el tiempo de ciclo
    conexion = Conexion(baseDeDatos)
    result = conexion.updateInterseccionTime(interseccion_id, tCiclo)
    conexion.cerrarConexion()

    return jsonify({"mensaje": "Tiempo de ciclo actualizado correctamente"}), 200

@app.route('/getUsuario/<string:usuario>', methods=['GET'])
def getUsuario(usuario):
    conexion = Conexion(baseDeDatos)
    result = conexion.getUsuario(usuario)
    conexion.cerrarConexion()
    return jsonify(result)

@app.route('/new_user', methods=['POST'])
def create_user():
    data = request.json
    usuario = data.get("usuario")
    contrasena = data.get("contrasena")
    nombre = data.get("nombre")
    
    # Asegúrate de que se proporcionan todos los campos
    if not usuario or not contrasena or not nombre:
        return jsonify({"error": "Todos los campos son requeridos"}), 400

    # Conectar a la base de datos y crear el usuario
    conexion = Conexion(baseDeDatos)
    conexion.createUsuario(usuario, contrasena, nombre)
    conexion.cerrarConexion()

    return jsonify({"message": "Usuario creado exitosamente"}), 201


if __name__ == '__main__':
    app.run(debug=True)
