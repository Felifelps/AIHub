from constants import TEMPLATE
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()


class Agent:

    _llm = None

    def __init__(self):
        self.__chain = (
            PromptTemplate(
                input_variables=[
                    "language",
                    "question",
                    "answer"
                ],
                template=TEMPLATE
            ) | self._llm | StrOutputParser()
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
