import os
from ai.gemini_agent import GeminiAgent
from ai.tools.mercado_livre_tool import MercadoLivreSearchTool
from langchain.agents import initialize_agent, AgentType
from langchain_core.prompts import PromptTemplate


class MercadoLivreAgent(GeminiAgent):
    _prompt_template = PromptTemplate.from_template(
        """
        Busque as melhores ofertas do mercado livre usando a sua ferramenta
        para a buscas a partir da 
        query "{query}" e ordene as ofertas encontradas por
        melhor custo-benefício.

        Não responda em JSON, apenas liste as melhores ofertas.
        Responda sempre em português brasileiro.
        """
    )

    def __init__(self):
        self._agent = initialize_agent(
            tools=[
                MercadoLivreSearchTool()
            ],
            llm=self._llm,
            agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
            verbose=True,
        )

    def run(self, query):
        return self._agent.run(
            self._prompt_template.format(query=query)
        )
