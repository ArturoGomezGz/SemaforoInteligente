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

@app.route('/updateTCiclo/<int:interseccion_id>/<int:tCiclo>', methods=['GET','PUT'])
def updateTCiclo(interseccion_id,tCiclo):
    conexion = Conexion(baseDeDatos)
    result = conexion.updateInterseccionTime(interseccion_id,tCiclo)
    conexion.cerrarConexion()
    return jsonify({'mensaje': 'Tiempo de ciclo actualizado correctamente'}), 200

@app.route('/getUsuario/<str:usuario>', methods=['GET'])
def get_ultimo_registro(usuario):
    conexion = Conexion(baseDeDatos)
    result = conexion.getUsuario(usuario)
    conexion.cerrarConexion()
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
