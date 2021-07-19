from flask_restful import Resource
from flask import Flask, request
from tools.authentication import auth
from model.padoca import Padoca
from model.instancias import Instancias

class Init(Resource):

    #curl --header "Content-Type: application/json"   --request POST  --data '{"nFornecedores": "3", "nClients": "5", "custoFornecedorCliente":[["1","2","3"],["5","7","5"],["3","9","2"],["9","1","4"],["1","154","13"]],"custoFornecedor": ["10","2","7"]}'   http://localhost:5000/api/v1/init

    def post(self):
        data = request.get_json(force=True)
        nClientes = int(data['nClients'])
        nFornecedores = int(data['nFornecedores'])

        custoFornecedorCliente = []
        for i in range(nClientes):
            custoFornecedorCliente.append([])
            dataCusto = data['custoFornecedorCliente']
            for j in range(nFornecedores):
                custoFornecedorCliente[i].append(int(dataCusto[i][j]))

        custoFornecedor = []
        datacusto = data['custoFornecedor']
        for i in range(nFornecedores):
            custoFornecedor.append(dataCusto[i])

        padoca = Padoca(nClientes, nFornecedores, custoFornecedorCliente, custoFornecedor)
        padoca.createFileInstance()
        padoca.run()

        Instancias.addPadoca(padoca, padoca.id)

        return {"id": padoca.id, "password": padoca.password}

