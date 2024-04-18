"""House price prediction service"""

from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return 'Housing price service. Use /predict endpoint'


@app.route("/predict")
def predict():
    """Dummy service"""
    area = request.args.get("area")

    price = 5_000_000
    return f'{price}'


if __name__ == "__main__":
    app.run(host='0.0.0.0')
