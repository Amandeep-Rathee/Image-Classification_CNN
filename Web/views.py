from web import api
import joblib
from PIL import Image
from flask import request, jsonify
from web.config import Y_labels
from flask_restful import Resource
from collections.abc import Mapping

class Predict(Resource):
    def post(self):
        model = joblib.load('model.pkl')
        input_image = request.files.get('url')

        o = Image.open(image_file).convert('RGB')
        o = o.resize((32, 32))
        o = o.convert('RGB')
        o_value = np.asarray(o.getdata(), dtype=np.int).reshape((32, 32, 3))
        o_value = o_value.flatten()
        o_value = o_value.reshape(-1,32,32,3)

        y_predict = np.argmax(model.predict(o_value), axis=-1)
        prediction = Y_labels[y_predict[0]]  

        return jsonify({'prediction': prediction})

