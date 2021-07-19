from flask_restful import Resource
from flask import Flask, request
from tools.authentication import auth
from model.padoca import Padoca

class GetSol(Resource):
    @auth.login_required
    def get(self):
        return {"meaning_of_life": 42}
