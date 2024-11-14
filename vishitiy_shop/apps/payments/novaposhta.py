from functools import lru_cache

import requests
from django.conf import settings


class NovaPoshta:
    def __init__(self):
        self.api_url = "https://api.novaposhta.ua/v2.0/json/"
        self.api_key = settings.NOVAPOSHTA_KEY

    @lru_cache(maxsize=32)
    def send(self, model_name: str, method: str, **params):
        resp = requests.post(
            self.api_url,
            json={
                "apiKey": self.api_key,
                "modelName": model_name,
                "calledMethod": method,
                "methodProperties": params,
            },
            headers={"Content-Type": "application/json"},
        )

        return resp.json()

    def get_cities(self, **params):
        return self.send("Address", "getCities", **params)

    def search_cities(self, **params):
        return self.send("AddressGeneral", "searchSettlements", **params)

    def get_post_offices(self, **params):
        return self.send("AddressGeneral", "getWarehouses", **params)


nova_poshta = NovaPoshta()
