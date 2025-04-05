# AIHub
## Descrição do Projeto
O AIHub é um repositório de código que visa criar uma plataforma de inteligência artificial para geração de conteúdo, correção de código e outras funcionalidades relacionadas à IA. O projeto é desenvolvido em Python e utiliza bibliotecas como LangChain, OpenAI e Groq para implementar as funcionalidades de IA.

## Estrutura dos Arquivos
O repositório contém os seguintes arquivos e pastas:

* `ai`: pasta que contém os arquivos relacionados à inteligência artificial, incluindo os agentes e os modelos de IA.
* `agents`: pasta que contém os arquivos dos agentes de IA, incluindo o `AIHubAgent`, `CodeCorrectorAgent` e `ReadmeGeneratorAgent`.
* `utils`: pasta que contém os arquivos de utilidade, incluindo funções para validação de nomes de coleção e conversão de nomes de arquivo.
* `constants`: arquivo que contém constantes utilizadas no projeto, incluindo os modelos de IA e as configurações de banco de dados.
* `requirements.txt`: arquivo que contém as dependências do projeto.
* `streamlit`: pasta que contém os arquivos relacionados à interface do usuário, incluindo o `app.py` e o `page_utils.py`.

## Instruções de Configuração e Execução
Para configurar e executar o projeto, siga os passos abaixo:

1. Instale as dependências necessárias utilizando o comando `pip install -r requirements.txt`.
2. Configure as variáveis de ambiente necessárias, incluindo a chave de API do Google e a chave de API do OpenAI.
3. Execute o comando `streamlit run app.py` para iniciar a interface do usuário.

## Exemplos de Uso
O AIHub pode ser utilizado para diversas finalidades, incluindo:

* Geração de conteúdo: o `AIHubAgent` pode ser utilizado para gerar conteúdo baseado em um conjunto de dados.
* Correção de código: o `CodeCorrectorAgent` pode ser utilizado para corrigir código-fonte baseado em um conjunto de regras.
* Geração de documentos: o `ReadmeGeneratorAgent` pode ser utilizado para gerar documentos baseados em um conjunto de dados.

## Requisitos
O projeto requer as seguintes dependências:

* Python 3.8 ou superior
* LangChain 0.3.14 ou superior
* OpenAI 1.59.9 ou superior
* Groq 0.16.0 ou superior
* Streamlit 1.41.1 ou superior

## Contribuição
Para contribuir com o projeto, siga os passos abaixo:

1. Faça um fork do repositório.
2. Crie uma branch para sua contribuição.
3. Realize as alterações necessárias.
4. Envie um pull request para o repositório principal.

## Licença
O projeto é licenciado sob a licença MIT.