import time
from multiprocessing import Pool
import requests


endpoint = 'http://127.0.0.1:5000/predict'


def do_request(area: int) -> str:
    data = {'area': area}
    t0 = time.time()
    resp = requests.post(endpoint, json=data).text
    t = time.time() - t0
    return f'Waited {t:0.2f} sec ' + resp 


def test_10():
    with Pool(10) as p:
        print(*p.map(do_request, range(10, 110, 10)))
    

if __name__ == '__main__':
    test_10()
