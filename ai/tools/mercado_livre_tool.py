from langchain.tools import BaseTool
from services.mercado_livre_api import MercadoLivreClient


class MercadoLivreSearchTool(BaseTool):
    def __init__(self):
        super().__init__(
            name="mercado_livre_search",
            description="Busca ofertas no Mercado Livre."
        )
        self.__client = MercadoLivreClient()

    def _run(self, query):
        return str(self.__client.search_products(query))

    def _arun(self, query):
        raise NotImplementedError("Busca assíncrona não implementada.")
