import os
from constants import TEMPLATE
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()

class Agent:

    def __init__(self):
        self.__model = 'gpt-3.5-turbo'
        self.__llm = ChatOpenAI(
            model=self.__model,
            api_key=os.getenv("OPENAI_API_KEY")
        )
        self.__chain = (
            PromptTemplate(
                input_variables=[
                    "language",
                    "question",
                    "answer"
                ],
                template=TEMPLATE
            )
            | self.__llm
            | StrOutputParser()
        )

    def run(self, language, question, answer):
        try:
            return self.__chain.invoke({
                'language': language,
                'question': question,
                'answer': answer,
            })
        except Exception as e:
            print(e)
            return "An error ocurred while using AI"
