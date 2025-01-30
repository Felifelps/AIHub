from ai.especific_agents import BASE_AGENT_CLASS
from langchain_core.prompts import PromptTemplate
from langchain_community.document_loaders import GithubFileLoader


class ReadmeGeneratorAgent(BASE_AGENT_CLASS):
    _prompt_template = PromptTemplate.from_template(
        """
        **Instruções para a IA:**  
        Você é um especialista em documentação de projetos de software. Sua tarefa é criar um arquivo `README.md` completo para um repositório de código, com base nos arquivos fornecidos.  

        **Regras para o conteúdo do `README.md`:**  
        1. **Título do Repositório:**  
        - Use um título claro e relacionado ao objetivo do projeto.  

        2. **Descrição do Projeto:**  
        - Forneça uma visão geral do projeto, explicando seu propósito, funcionalidades principais e caso de uso.  

        3. **Estrutura dos Arquivos:**  
        - Liste e descreva os arquivos fornecidos no repositório. Explique suas funções no contexto do projeto.  

        4. **Instruções de Configuração e Execução:**  
        - Inclua passos detalhados para configurar, instalar dependências e executar o projeto.  

        5. **Exemplos de Uso:**  
        - Adicione exemplos práticos ou casos de uso para ajudar os usuários a entenderem como utilizar o projeto.  

        6. **Requisitos:**  
        - Liste as dependências e versões mínimas de ferramentas ou bibliotecas necessárias para o funcionamento do projeto.  

        7. **Contribuição:**  
        - Forneça diretrizes para contribuir com o projeto, caso aplicável.  

        8. **Licença:**  
        - Inclua informações sobre a licença, se aplicável.  

        **Nota Importante:**  
        - Seja claro, conciso e organizado.  
        - Use formatação Markdown, incluindo títulos, listas e blocos de código, onde necessário.
        - Não coloque a resposta entre "```"s.
        
        **Nome do Repositório:** {repo_name}

        **Lista de Arquivos no Repositório:**
        {data}  
        """
    )

    def run(self, repo_name, branch, extensions=['.md']):
        try:
            loader = GithubFileLoader(
                repo=repo_name, # username/project_name
                branch=branch,
                github_api_url="https://api.github.com",
                file_filter=lambda file_path: any(
                    (file_path.endswith(ext) for ext in extensions)
                )
            )

            documents = loader.load()
            data = "\n".join([doc.page_content for doc in documents])

            return super().run(
                repo_name=repo_name,
                data=data
            )
        except Exception as e:
            print(e)
            return "An error ocurred while using AI"
