from pprint import pprint
from ai.openai_agent import OpenaiAgent
from ai.gemini_agent import GeminiAgent
from ai.rag.rag_agent import RAGAgent
from ai.rag.vector_store import VectorStore


#VectorStore.add_pdf('dnd', 'C:\\Users\\Felipe\\Área de Trabalho\\D&D 5e - Básico.pdf')

class DnDAgent(RAGAgent, GeminiAgent):
    pass


agent = DnDAgent('dnd')
while True:
    try:
        a = agent.run(input('Ask: '))
        print(a)
    except KeyboardInterrupt:
        break
