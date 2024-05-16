import unittest
import requests


class TestApi(unittest.TestCase):
    def test_home(self):
        resp = requests.get('http://127.0.0.1:5000')
        self.assertIn('Housing price service', resp.text)

    def test_api(self):
        data = {'area': 42}
        resp = requests.post('http://127.0.0.1:5000/predict', json=data)
        self.assertIn('price', resp.text)


if __name__ == '__main__':
    unittest.main()
