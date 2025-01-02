LANGUAGES = [
    "Pseudocódigo",
    "Python"
]

TEMPLATE = """
Dada a questão, você deve:
1. Analisar a resposta fornecida e identificar se está correta.
2. Se houver erros na resposta, liste-os detalhadamente.
3. Se a resposta estiver correta, responda com: **"Resposta Correta."**

Formato esperado de saída:
- Se houver erros:
  ```
  Erros encontrados:
  1. {{Descrição do erro 1}}
  2. {{Descrição do erro 2}}
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

OPENAI_MODEL = "gpt-3.5-turbo"
GEMINI_MODEL = "gemini-1.5-flash-8b"
