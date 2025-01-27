from ai.agent import Agent
from ai.rag.vector_store import VectorStore
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain
from langchain_core.prompts import ChatPromptTemplate


class RAGAgent(Agent):
    _prompt_template = ChatPromptTemplate.from_messages(
        {
            ('system', 'Você é um assistente especializado que responde perguntas de forma clara e objetiva. Use as informações fornecidas no contexto abaixo para elaborar suas respostas, ou use mais contextos para pesquisar. Caso não encontre uma resposta no contexto, explique que a informação não está disponível e evite inventar dados. Contexto: {context}'),
            ('human', '{input}')
        }
    )

    def __init__(self, collection_name):
        retriever = VectorStore.get_collection(collection_name)
        question_answer = create_stuff_documents_chain(
            llm=self._llm,
            prompt=self._prompt_template
        )

        self._chain = create_retrieval_chain(
            retriever=retriever,
            combine_docs_chain=question_answer
        )

    def invoke(self, **input_variables):
        return super().invoke(**input_variables).get('answer')

    def run(self, input):
        return super().run(input=input)
