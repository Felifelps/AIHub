from ai.gemini_agent import GeminiAgent
from langchain_core.prompts import PromptTemplate


class CodeCorrectorAgent(GeminiAgent):
    _prompt_template = PromptTemplate.from_template(
        """
        Dada a questão, você deve:
        1. Analisar a resposta fornecida e identificar se está correta.
        2. Se houver erros na resposta, liste-os detalhadamente.
        3. Se a resposta estiver correta, responda com: **"Resposta Correta."**

        Formato esperado de saída:
        - Se houver erros:
        ```
        Erros encontrados:
        1. "Descrição do erro 1"
        2. "Descrição do erro 2"
        ```
        - Se a resposta estiver correta:
        "Resposta Correta."

        Certifique-se de seguir este padrão rigorosamente.

        Questão: {question}
        Resposta (na linguagem {language}):
        ```
        {answer}
        ```
        """
    )
