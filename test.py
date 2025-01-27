from pprint import pprint
from ai.openai_agent import OpenaiAgent
from ai.gemini_agent import GeminiAgent
from ai.rag.rag_agent import RAGAgent
from ai.rag.vector_store import VectorStore


#VectorStore.add_pdf('Dnd', "C:\\Users\\Felipe\\Área de Trabalho\\D&D 5e - Básico.pdf")

print(VectorStore.list_collections())

class TestAgent(RAGAgent, GeminiAgent):
    pass


agent = TestAgent('LivroIP')
while True:
    try:
        a = agent.run(input('Ask: '))
        print(a)
    except KeyboardInterrupt:
        break
