import json
import os
import requests


class MercadoLivreClient:

    def __init__(self):
        access_token = os.environ['MERCADO_LIVRE_SECRET_KEY']
        self.__headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {access_token}',
        } 
        self.__base_url = "https://api.mercadolibre.com/sites/MLA"

    def search_products(self, query):
        query = query.replace(" ", "%20")
        try:
            response = requests.get(
                url=f"{self.__base_url}/search?q={query}",
                headers=self.__headers
            )
            if response.status_code != 200:
                return f'Error on request {response.status_code}'
            return json.dumps(
                response.json()['results'],
                indent=4
            )
        except Exception as e:
            print(e)
            return 'An error ocurred'
