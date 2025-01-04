from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser


load_dotenv()


class Agent:

    _llm = None
    _prompt_template = None

    def __init__(self):
        self._chain = (
            self._prompt_template | self._llm | StrOutputParser()
        )

    def run(self, **input_variables):
        try:
            return self._chain.invoke(input_variables)
        except Exception as e:
            print(e)
            return "An error ocurred while using AI"
