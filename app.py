import urllib.request
import urllib.parse
import json
from requests import put, get

from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class GrammarCheck(Resource):
    def get(self):
        return {'hello': request.form['username']}
    def put(self):
        return {"put_hello": request.form['username']}
    def post(self):
        return {"posted_hello": "res"}


api.add_resource(GrammarCheck, '/grammarCheck')


if __name__ == "__main__":
    app.run()
