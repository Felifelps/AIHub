from dotenv import load_dotenv
from langchain.globals import set_llm_cache
from langchain_community.cache import SQLiteCache
from langchain_core.output_parsers import StrOutputParser


load_dotenv()
set_llm_cache(SQLiteCache(database_path='cache.db'))


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
