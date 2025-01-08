from pprint import pprint
from ai.mercado_livre_agent import MercadoLivreAgent
from services.mercado_livre_api import MercadoLivreClient


"""agent = MercadoLivreAgent()

a = agent.run("Notebook Dell")

print(a)"""

search = MercadoLivreClient()

result = search.search_products('Kalimba')

#print(result)
pprint(result)