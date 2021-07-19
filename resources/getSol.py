from flask_restful import Resource
from flask import Flask, request
from tools.authentication import auth
from model.padoca import Padoca

class GetSol(Resource):
    @auth.login_required

    #curl --user 31:s6Svw4J02OtdjHfh http://localhost:5000/api/v1/getSol
    def get(self):
        return {"meaning_of_life": 42}
