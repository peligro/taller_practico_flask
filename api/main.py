from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_mysqldb import MySQL

app = Flask(__name__)
api = Api(app)
app.secret_key = "123456"

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'peligro'
app.config['MYSQL_PASSWORD'] = '123456'
app.config['MYSQL_DB'] = 'pruebas_python'

mysql = MySQL(app)


class Productos(Resource):
    
    
    def get(self):
        cursor = mysql.connection.cursor()
        cursor.execute("select * from productos;")
        datos = cursor.fetchall()
        payload = []
        content = []
        for dato in datos:
            content = {'id': dato[0], 'titulo': dato[1], 'descripcion': dato[2], 'precio': dato[3], 'fecha': dato[3]}
            payload.append(content)
        return jsonify(payload)
    

    def post(self):
        cursor = mysql.connection.cursor()
        cursor.execute("insert into productos values (null, %s, %s, %s, now());", (
                  request.json['titulo'],
                  request.json['descripcion'],
                  request.json['precio']
        ))
        cursor.connection.commit()
        return jsonify({"estado": "producto creado exitosamente!!!"})


    def put(self):
        cursor = mysql.connection.cursor()
        cursor.execute("update productos set titulo=%s, descripcion=%s, precio=%s where id=%s;", (
                  request.json['titulo'],
                  request.json['descripcion'],
                  request.json['precio'],
                  request.json['id']
        ))
        cursor.connection.commit()
        return jsonify({"estado": "producto modificado exitosamente!!!"})


    def delete(self):
        return jsonify({"estado": "hola desde delete"})


class ProductosId(Resource):

    def get(self, id):
        cursor = mysql.connection.cursor()
        cursor.execute(f"select * from productos where id='{id}';")
        datos = cursor.fetchall()
        content = []
        for dato in datos:
            content = {'id': dato[0], 'titulo': dato[1], 'descripcion': dato[2], 'precio': dato[3], 'fecha': dato[3]}
        return jsonify(content)



api.add_resource(Productos, '/productos')
api.add_resource(ProductosId, '/productos/<id>')


if __name__ == '__main__':
     app.run(debug=True)