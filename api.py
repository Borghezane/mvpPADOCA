from flask import Flask
from flask_restful import Api
from resources.init import Init
from resources.getSol import GetSol
from model.padoca import Padoca

instancias = {}

app = Flask(__name__)
api = Api(app, prefix="/api/v1")

# add init resource
api.add_resource(Init, '/init')

# add getSol resource
api.add_resource(GetSol, '/getSol')

if __name__ == '__main__':
    Padoca.getUpdateId()
    app.run(debug=True)
