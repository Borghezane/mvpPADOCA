from flask_restful import Resource
from flask import Flask, request
from tools.authentication import auth
from model.padoca import Padoca
import os.path
import json

class GetSol(Resource):
    @auth.login_required

    #curl --user 31:s6Svw4J02OtdjHfh http://localhost:5000/api/v1/getSol
    def post(self):
        data = request.get_json(force=True)
        padid = int(data['id'])
        if os.path.isfile('data/PadocaRuns/'+str(padid)+'.prun'):
            arq = open("data/PadocaRuns/"+str(padid)+".prun","r", encoding="utf-8")
            content = arq.readline()
            return json.loads(content)
        else:
            return {"custo": "-inf", "encerrado": "false", "solucao": "[]"}
