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

    def invoke(self, **input_variables):
        return self._chain.invoke(input_variables)

    def run(self, **input_variables):
        return self.invoke(**input_variables)
