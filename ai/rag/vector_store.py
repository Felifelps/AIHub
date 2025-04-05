import constants as cs
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_community.document_loaders import PyPDFLoader, GithubFileLoader
from langchain_openai import OpenAIEmbeddings


class VectorStore:
    __text_sppliter = RecursiveCharacterTextSplitter(
        chunk_size=cs.CHUNK_SIZE,
        chunk_overlap=cs.CHUNK_OVERLAP
    )
    __embedding = OpenAIEmbeddings()

    @classmethod
    def delete_collection(cls, collection_name):
        return Chroma(
            embedding_function=cls.__embedding,
            collection_name=collection_name,
            persist_directory=cs.PERSIST_VECTOR_STORE_DIR
        ).delete_collection()

    @classmethod
    def get_collection(cls, collection_name):
        return Chroma(
            embedding_function=cls.__embedding,
            collection_name=collection_name,
            persist_directory=cs.PERSIST_VECTOR_STORE_DIR
        ).as_retriever()

    @classmethod
    def list_collections(cls):
        chroma_client = Chroma(
            embedding_function=cls.__embedding,
            persist_directory=cs.PERSIST_VECTOR_STORE_DIR
        )
        return [collection.name for collection in chroma_client._client.list_collections() if collection.name != 'langchain']

    @classmethod
    def add_pdf(cls, collection_name, pdf_path):
        return cls.__add_data_to_collection(
            collection_name=collection_name,
            docs=cls.__get_pdf_docs(pdf_path)
        )

    @classmethod
    def __get_pdf_docs(cls, pdf_path):
        docs = PyPDFLoader(pdf_path).load()
        if not docs:
            raise Exception('The PDF file has no text data')
        return docs

    @classmethod
    def add_github_repo(cls, collection_name, repo_name, branch, extensions=['.md']):
        return cls.__add_data_to_collection(
            collection_name=collection_name,
            docs=cls.__get_github_repo_docs(repo_name, branch, extensions)
        )
    
    @classmethod
    def __get_github_repo_docs(cls, repo_name, branch, extensions):
        loader = GithubFileLoader(
            repo=repo_name, # username/project_name
            branch=branch,
            github_api_url="https://api.github.com",
            file_filter=lambda file_path: any(
                (file_path.endswith(ext) for ext in extensions)
            )
        )

        return loader.load()

    @classmethod
    def __add_data_to_collection(cls, collection_name, docs):
        chunks = cls.__text_sppliter.split_documents(docs)
        return Chroma.from_documents(
            documents=chunks,
            embedding=cls.__embedding,
            collection_name=collection_name,
            persist_directory=cs.PERSIST_VECTOR_STORE_DIR
        ).as_retriever()
