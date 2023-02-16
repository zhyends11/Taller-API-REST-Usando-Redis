from flask import Flask, request, jsonify
from flask_restful import Api, Resource
import redis

app = Flask(__name__)
api = Api(app)
r = redis.Redis(host='localhost', port=6379, db=0)

class Estudiante(Resource):
    def get(self, codigo_estudiante):
        estudiante = r.hgetall(codigo_estudiante)
        return jsonify(estudiante)

    def post(self, codigo_estudiante):
        nombre = request.form['nombre']
        email = request.form['email']
        carrera = request.form['carrera']
        nivel = request.form['nivel']
        r.hmset(codigo_estudiante, {'nombre': nombre, 'email': email, 'carrera': carrera, 'nivel': nivel})
        return '', 201

api.add_resource(Estudiante, '/estudiantes/<string:codigo_estudiante>')

if __name__ == '__main__':
    app.run(debug=True)
