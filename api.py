from flask import Flask
from flask_restful import Api, Resource, reqparse
import json

app = Flask(__name__)
api = Api(app)

contato = [
    {
        "name": "Mariana",
        "telefone": 987654321
    }, 
    {
        "name": "Nathalia",
        "telefone": 912345678
    },
     {
        "name": "Fernando",
        "telefone": 987651234
    }, 
     {
        "name": "Robson",
        "telefone": 912348765
    }
]

class Users(Resource): 
    def get(self, name):
        for users in contato:
            if(name == users["name"]):
                return users, 200
        return "Usuario nao encontrado", 404

    def post(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("telefone")
        args = parser.parse_args()
        
        for users in contato:
            if(name == users["name"]):
                return "Usuario com esse nome "+name+" ja existe", 400
        users = {
            "name": name,
            "telefone": args["telefone"],
        }
        contato.append(users)
        return users, 201

    def put(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("telefone")
        args = parser.parse_args()
        
        for users in contato:
            if(name == users["name"]):
                users["telefone"] = args["telefone"]
                return users, 200
        users = {
            "name": name,
            "telefone": args["telefone"],
        }
        contato.append(users)
        return users, 201

    def delete(self, name):
        global contato
        contato = [users for users in contato if users["name"] != name]
        return name+" foi deletado com sucesso.", 200

#Para rodar a api
api.add_resource(Users, "/users/<string:name>")

#app.run(debug=True, port=80)
app.run(host="0.0.0.0", port=80) #Config AWS
