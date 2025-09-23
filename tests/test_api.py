 # tests/test_api.py
import unittest
import requests
import json
import os
import sys
# Si aggiunge la cartella principale al path per importare l'app
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class TestApi(unittest.TestCase):

    def setUp(self):
        """Definiamo l'URL base della nostra API."""
        self.base_url = "http://localhost:5000"
        print(f"\n[Integration Test] Testing API at {self.base_url}")

    def test_predict_endpoint_positive(self):
        """Testa l'endpoint /predict con una recensione positiva."""
        url = f"{self.base_url}/predict"
        payload = {"review": "This is a great and amazing product"}
        response = requests.post(url, json=payload)
        
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['sentiment'], 'positive')
        print(f"[Integration Test] /predict Positive -> OK (Status: {response.status_code})")

    def test_predict_endpoint_negative(self):
        """Testa l'endpoint /predict con una recensione negativa."""
        url = f"{self.base_url}/predict"
        payload = {"review": "This is a bad product"}
        response = requests.post(url, json=payload)
        
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['sentiment'], 'negative')
        print(f"[Integration Test] /predict Negative -> OK (Status: {response.status_code})")

    def test_predict_endpoint_bad_request(self):
        """Testa che l'endpoint restituisca un errore 400 se 'review' è mancante."""
        url = f"{self.base_url}/predict"
        payload = {"text": "This is a bad request"} # Chiave sbagliata
        response = requests.post(url, json=payload)
        
        self.assertEqual(response.status_code, 400)
        print(f"[Integration Test] /predict Bad Request -> OK (Status: {response.status_code})")

    def test_metrics_endpoint(self):
        """Testa che l'endpoint /metrics sia raggiungibile e restituisca del testo."""
        url = f"{self.base_url}/metrics"
        response = requests.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertIn("http_requests_total", response.text)
        print(f"[Integration Test] /metrics -> OK (Status: {response.status_code})")


if __name__ == '__main__':
    unittest.main()
