# utils/api_client.py
import requests
from .config import BASE_URL, HEADERS

def post(endpoint, payload):
    return requests.post(f"{BASE_URL}{endpoint}", headers=HEADERS, json=payload)

def get(endpoint):
    return requests.get(f"{BASE_URL}{endpoint}", headers=HEADERS)

def put(endpoint, payload):
    return requests.put(f"{BASE_URL}{endpoint}", headers=HEADERS, json=payload)

def delete(endpoint):
    return requests.delete(f"{BASE_URL}{endpoint}", headers=HEADERS)