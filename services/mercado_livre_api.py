import asyncio
import os
import requests


class MercadoLivreClient:

    def __init__(self):
        access_token = os.environ['MERCADO_LIVRE_SECRET_KEY']
        self.__headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {access_token}',
        } 
        self.__base_url = "https://api.mercadolibre.com/sites/MLB"
        self.__review_url = "https://api.mercadolibre.com/reviews/item"

    def search_products(self, query):
        query = query.replace(" ", "%20")
        try:
            response = requests.get(
                url=f"{self.__base_url}/search?q={query}",
                headers=self.__headers
            )
            if response.status_code != 200:
                return f'Error on request {response.status_code}'
            data = response.json()['results']
            #return asyncio.run(self.__format_products(data))
            return asyncio.run(self.__get_reviews(data[0].get('id')))
        except Exception as e:
            print(e)
            return 'An error ocurred'

    async def __format_products(self, data):
        result = []
        for product in data:
            result.append({
                'title': product.get('title'),
                'price': product.get('price'),
                **(await self.__get_reviews(product.get('id')))
            })

        return result

    async def __get_reviews(self, item_id):
        try:
            response = requests.get(
                url=f"{self.__review_url}/{item_id}",
                headers=self.__headers
            )
            if response.status_code != 200:
                return f'Error on request: {response.status_code}'
            return response.json()
        except Exception as e:
            print(e)
            return 'An error ocurred'
