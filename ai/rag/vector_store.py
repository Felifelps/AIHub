import constants as cs
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import OpenAIEmbeddings


# TODO: ValueError: Expected collection name that (1) contains 3-63 characters, (2) starts and ends with an alphanumeric character, (3) otherwise contains only alphanumeric characters, underscores or hyphens (-), (4) contains no two consecutive periods (..) and (5) is not a valid IPv4 address, got IP
# Code to check if collection name fits those requirements

class VectorStore:
    __text_sppliter = RecursiveCharacterTextSplitter(
        chunk_size=cs.CHUNK_SIZE,
        chunk_overlap=cs.CHUNK_OVERLAP
    )
    __embedding = OpenAIEmbeddings()

    @classmethod
    def get_collection(cls, collection_name):
        return Chroma(
            embedding_function=cls.__embedding,
            collection_name=collection_name,
            persist_directory=cs.PERSIST_VECTOR_STORE_DIR
        ).as_retriever()

    @classmethod
    def get_collections(cls, collection_name):
        return None

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
            raise Exception('The pdf has no text data')
        return docs

    @classmethod
    def __add_data_to_collection(cls, collection_name, docs):
        chunks = cls.__text_sppliter.split_documents(docs)
        return Chroma.from_documents(
            documents=chunks,
            embedding=cls.__embedding,
            collection_name=collection_name,
            persist_directory=cs.PERSIST_VECTOR_STORE_DIR
        ).as_retriever()
