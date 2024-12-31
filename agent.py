import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate


load_dotenv()

class Agent:

    def __init__(self):
        self.__model = 'gpt-3.5-turbo'
        self.__llm = ChatOpenAI(
            model=self.__model,
            api_key=os.getenv("OPENAI_API_KEY")
        )
        template = """
            **Você é um especialista altamente qualificado em programação.**  
            Sua principal tarefa é avaliar a precisão da resposta fornecida para
            uma questão específica tambpem fornecida e retornar os apenas os 
            erros cometidos pelo usuário, caso hajam.

            - **Se a resposta não contiver erros**, inicie sua avaliação com: **"Resposta Correta."**
            - **Se a resposta contiver erros**, inicie com: **"Resposta Incorreta."**, e então:
                - Identifique os erros cometidos, sejam de lógica ou de sintaxe.
                - Não dê sugestões de resposta.

            Questão: {question}
            Responda usando {language}.
            Resposta:
            ```
            {answer}
            ```
            """
        self.__chain = (
            PromptTemplate(
                input_variables=[
                    "language",
                    "question",
                    "answer"
                ],
                template=template
            )
            | self.__llm
        )

    def run(self, language, question, answer):
        try:
            return self.__chain.invoke({
                'language': language,
                'question': question,
                'answer': answer,
            }).content
        except Exception as e:
            print(e)
            return "An error ocurred while using AI"
