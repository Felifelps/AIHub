# AIHub

Este projeto é uma aplicação web desenvolvida com Flet que utiliza a biblioteca LangChain para integrar modelos de IA, como Gemini e OpenAI, para realizar correção de código e geração de arquivos README.

## Descrição do Projeto

O AIHub oferece duas funcionalidades principais:

* **Correção de Código:** Permite ao usuário inserir uma questão e uma resposta em uma linguagem específica (Python ou Pseudocódigo), e o sistema analisa a resposta quanto à correção, identificando erros e fornecendo feedback.
* **Geração de README:** Permite a geração automática de arquivos README.md para repositórios GitHub, com base nos arquivos do repositório.

O projeto visa simplificar tarefas comuns de desenvolvimento de software, como a análise de respostas de modelos de IA e a criação de documentação.

## Estrutura dos Arquivos

* **`ai/agent.py`:** Classe base para os agentes de IA, contendo o método `run` para a execução das chamadas aos modelos de IA.
* **`ai/gemini_agent.py`:** Classe derivada de `Agent` que utiliza o modelo Gemini.
* **`ai/code_corrector_agent.py`:** Classe derivada de `GeminiAgent` especializada na correção de código.
* **`ai/readme_generator_agent.py`:** Classe derivada de `GeminiAgent` especializada na geração de arquivos README.
* **`ai/openai_agent.py`:** Classe derivada de `Agent` que utiliza o modelo OpenAI.
* **`constants.py`:**  Arquivo contendo constantes, como URLs e chaves de API.
* **`ui/code_corrector_page.py`:**  Define a página para correção de código na interface.
* **`ui/readme_generator_page.py`:** Define a página para geração de README na interface.
* **`ui/view.py`:** Classe base para as páginas da interface.
* **`main.py`:** Arquivo principal que inicia a aplicação Flet.
* **`.env`:** Arquivo para armazenar as chaves API e tokens (GOOGLE_API_KEY, OPENAI_API_KEY, GITHUB_PERSONAL_ACCESS_TOKEN).

## Instruções de Configuração e Execução

1. **Instalação das Dependências:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configuração do Ambiente:**
   * Crie um arquivo `.env` no diretório raiz do projeto.
   * Adicione as chaves da API do Google e da OpenAI neste arquivo, além do token do GitHub, no seguinte formato:

     ```
     GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY
     OPENAI_API_KEY=YOUR_OPENAI_API_KEY
     GITHUB_PERSONAL_ACCESS_TOKEN=YOUR_GITHUB_TOKEN
     ```


3. **Execução:**
   ```bash
   python main.py
   ```

A aplicação será aberta em seu navegador.

## Exemplos de Uso

**Correção de Código:**

1. Digite a questão na caixa de texto "Digite sua Questão".
2. Selecione a linguagem da resposta na caixa de seleção "Linguagem".
3. Digite a resposta na caixa de texto "Digite sua Resposta".
4. Clique no botão "Corrigir".

O resultado da correção será exibido na caixa "Sua correção aparecerá aqui...".

**Geração de README:**

1. Digite o nome do repositório (username/repositório) na caixa de texto "Nome do repositório".
2. Digite o nome da branch na caixa de texto "Branch".
3. Digite as extensões de arquivos a serem consideradas, separadas por vírgula (ex.: `.py, .md, .js`).
4. Clique no botão "Gerar".

O arquivo README.md gerado será exibido na tela. Para copiar o conteúdo, clique no botão "Copiar".

(Este README foi gerado usando o ReadmeGenerator).

## Requisitos

* Python 3.9 ou superior
* Bibliotecas: `flet`, `langchain`, `google-generative-ai`, `langchain-google-genai`, `langchain-openai`, `python-dotenv`, `pyperclip`

## Contribuição

Contribuições são bem-vindas! Por favor, abra um issue ou um pull request para relatar problemas ou adicionar novos recursos.


## Licença

Até agora sem licença.
