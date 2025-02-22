from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': request.form['username']}
    def put(self):
        return {"put_hello": request.form['username']}
    def post(self):
        return {"posted_hello": "res"}

api.add_resource(HelloWorld, '/login')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
