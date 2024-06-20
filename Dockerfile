# syntax=docker/dockerfile:1

FROM python:3.9
WORKDIR /app

# dont change frequently
RUN pip3 install flask flask-cors flask_httpauth \
          scikit-learn python-dotenv joblib
COPY ./.env ./.env

# may be change frequently
COPY ./src/predict_app.py ./src/predict_app.py
COPY ./models/linear_regression_v01.joblib ./models/linear_regression_v01.joblib


CMD ["python3", "src/predict_app.py"]
EXPOSE 5000
