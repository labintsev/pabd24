"""
Test prediction web-service
If you have error: 503 Response, disable proxies in your requests
https://stackoverflow.com/questions/40430799/503-reponse-when-trying-to-use-python-request-on-local-website
"""
import time
import numpy as np
import requests
from dotenv import dotenv_values
import pandas as pd

endpoint = 'http://192.144.13.190:8000/predict'

config = dotenv_values(".env")
HEADERS = {"Authorization": f"Bearer {config['APP_TOKEN']}"}


def do_request(data: dict) -> tuple:
    t0 = time.time()
    resp = requests.post(
        endpoint,
        json=data,
        headers=HEADERS
    )
    resp = resp.json()
    t = time.time() - t0
    return t, resp['price']


def test_100():
    df = pd.read_csv('grads/test_100.csv')
    prices = df['price']
    df = df.drop(['price'], axis=1)
    records = df.to_dict('records')
    delays, pred_prices = [], []
    for row in records:
        t, price = do_request(row)
        delays.append(t)
        pred_prices.append(price)
    avg_delay = sum(delays) / len(delays)
    error = np.array(pred_prices) - prices.to_numpy()
    avg_error = np.mean(error)
    print(f'Avg delay: {avg_delay*1000} ms, avg error: {avg_error} RUB')


if __name__ == '__main__':
    test_100()
