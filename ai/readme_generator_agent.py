from ai.gemini_agent import GeminiAgent
from langchain_core.prompts import PromptTemplate


class ReadmeGeneratorAgent(GeminiAgent):
    _prompt_template = PromptTemplate.from_template(
        """
        Crie um readme completo para o repositório com os seguintes arquivos:

        {data}
        """
    )
