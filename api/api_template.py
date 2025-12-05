"""
Create an API template for Python with the standard library (request)
"""

import requests


class API:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def get(self, endpoint: str, params: dict = None):
        response = requests.get(self.base_url + endpoint, params=params)
        return response.json()

    def post(self, endpoint: str, data: dict = None):
        response = requests.post(self.base_url + endpoint, json=data)
        return response.json()

    def put(self, endpoint: str, data: dict = None):
        response = requests.put(self.base_url + endpoint, json=data)
        return response.json()
    def delete(self, endpoint: str):
        response = requests.delete(self.base_url + endpoint)
        return response.json()
