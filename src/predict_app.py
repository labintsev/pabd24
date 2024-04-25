"""House price prediction service"""

from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


def predict(in_data: dict) -> int:
    """ Predict house price from input data parameters.
    :param in_data: house parameters.
    :raise Error: If something goes wrong.
    :return: House price, RUB.
    :rtype: int
    """
    area = float(in_data['area'])
    AVG_PRICE = 200_000                 # RUB / m2
    return int(area * AVG_PRICE)


@app.route("/")
def home():
    return '<h1>Housing price service.</h1> Use /predict endpoint'


@app.route("/predict", methods=['POST'])
def predict_web_serve():
    """Dummy service"""
    in_data = request.get_json()
    price = predict(in_data)
    return {'price': price}


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
