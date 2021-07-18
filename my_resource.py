from flask_restful import Resource
from authentication import auth

class PrivateResource(Resource):
    @auth.login_required
    def get(self):
        return {"meaning_of_life": 42}
