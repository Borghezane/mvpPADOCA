from flask_httpauth import HTTPBasicAuth
from model.instancias import padocas

auth = HTTPBasicAuth()

@auth.verify_password
def verify(username, password):
    padid = username
    print(padid)
    print(password)
    print(len(padocas))

    for padid in padocas:
        print(padocas[padid].password)
        print(padocas[padid].id)

    if padid in padocas:
        return padocas[padid].password == password
    else:
        return False
