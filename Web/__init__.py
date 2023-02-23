from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api = Api(app)


from web.views import Predict
api.add_resource(Predict, '/predict')