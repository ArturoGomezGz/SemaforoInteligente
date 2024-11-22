from conexion.conexion import Conexion
from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

with open('./dbData.json', 'r') as archivo:
    baseDeDatos = json.load(archivo)

# GET Routes
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

@app.route('/ultimo_registro/<int:semaforo_id>', methods=['GET'])
def get_ultimo_registro(semaforo_id):
    conexion = Conexion(baseDeDatos)
    result = conexion.getUltimoRegistro(semaforo_id)
    conexion.cerrarConexion()
    return jsonify(result)

@app.route('/carSumRange/<int:idInterseccion>/<string:timeIni>/<string:timeFin>/<string:date>', methods=['GET'])
def get_car_sum(idInterseccion, timeIni, timeFin, date):
    conexion = Conexion(baseDeDatos)
    result = conexion.getSumByRange(idInterseccion, timeIni, timeFin, date)
    conexion.cerrarConexion()
    return jsonify(result)

@app.route('/carSumRangeByCiclos/<int:idSemaforo>/<string:timeIni>/<string:timeFin>/<string:date>', methods=['GET'])
def get_car_sum_ciclos(idSemaforo, timeIni, timeFin, date):
    conexion = Conexion(baseDeDatos)
    result = conexion.getCiclosRangeSemaforo(idSemaforo, timeIni, timeFin, date)
    conexion.cerrarConexion()
    return jsonify(result)

@app.route('/getUsuario/<string:usuario>', methods=['GET'])
def get_usuario(usuario):
    conexion = Conexion(baseDeDatos)
    result = conexion.getUsuario(usuario)
    conexion.cerrarConexion()
    return jsonify(result)

# POST Routes
@app.route('/new_user', methods=['POST'])
def create_user():
    data = request.json
    usuario = data.get("usuario")
    contrasena = data.get("contrasena")
    nombre = data.get("nombre")
    
    if not usuario or not contrasena or not nombre:
        return jsonify({"error": "Todos los campos son requeridos"}), 400

    conexion = Conexion(baseDeDatos)
    conexion.createUsuario(usuario, contrasena, nombre)
    conexion.cerrarConexion()

    return jsonify({"message": "Usuario creado exitosamente"}), 201

@app.route('/addMCiclo', methods=['POST'])
def add_mciclo():
    data = request.json
    idInterseccion = data.get("idInterseccion")
    dia = data.get("dia")
    hora = data.get("hora")
    
    if not idInterseccion or not dia or not hora:
        return jsonify({"error": "Todos los campos son requeridos"}), 400

    conexion = Conexion(baseDeDatos)
    conexion.agregarMCiclo(idInterseccion, dia, hora)
    conexion.cerrarConexion()

    return jsonify({"message": "Ciclo maestro agregado exitosamente"}), 201

@app.route('/addDCiclo', methods=['POST'])
def add_dciclo():
    data = request.json
    idMCiclo = data.get("idMCiclo")
    idSemaforo = data.get("idSemaforo")
    noCarros = data.get("noCarros")
    
    if not idMCiclo or not idSemaforo or not noCarros:
        return jsonify({"error": "Todos los campos son requeridos"}), 400

    conexion = Conexion(baseDeDatos)
    conexion.agregarDCiclo(idMCiclo, idSemaforo, noCarros)
    conexion.cerrarConexion()

    return jsonify({"message": "Ciclo detallado agregado exitosamente"}), 201

# PUT Routes
@app.route('/updateTCiclo', methods=['PUT'])
def update_t_ciclo():
    data = request.json
    interseccion_id = data.get("interseccion")
    tCiclo = data.get("tiempoCiclo")

    if interseccion_id is None or tCiclo is None:
        return jsonify({"error": "Todos los campos son requeridos"}), 400

    conexion = Conexion(baseDeDatos)
    conexion.updateInterseccionTime(interseccion_id, tCiclo)
    conexion.cerrarConexion()

    return jsonify({"mensaje": "Tiempo de ciclo actualizado correctamente"}), 200

@app.route('/adjustTime/<int:idSemaforo>', methods=['PUT'])
def adjust_time(idSemaforo):
    data = request.json
    tVerde = data.get("tVerde")
    tRojo = data.get("tRojo")

    if tVerde is None or tRojo is None:
        return jsonify({"error": "Todos los campos son requeridos"}), 400

    conexion = Conexion(baseDeDatos)
    conexion.ajustarTiempoSemaforo(idSemaforo, tVerde, tRojo)
    conexion.cerrarConexion()

    return jsonify({"mensaje": "Tiempos de semáforo actualizados correctamente"}), 200

# DELETE Routes
@app.route('/clearRecords', methods=['DELETE'])
def clear_records():
    conexion = Conexion(baseDeDatos)
    conexion.limpiarRegistros()
    conexion.cerrarConexion()

    return jsonify({"message": "Registros eliminados correctamente"}), 200

if __name__ == '__main__':
    app.run(debug=True)
