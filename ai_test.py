from ai.readme_generator_agent import ReadmeGeneratorAgent
from langchain_community.document_loaders import GithubFileLoader

agent = ReadmeGeneratorAgent()

loader = GithubFileLoader(
    repo="Felifelps/BibliotecaAcold",  # the repo name
    branch="master",  # the branch name
    github_api_url="https://api.github.com",
    file_filter=lambda file_path: file_path.endswith(
        ".py", 
    ),
)
documents = loader.load()

print(agent.run(
    data=[doc.page_content for doc in documents]
))