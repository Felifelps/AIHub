import os
from agent import Agent
from constants import OPENAI_MODEL
from langchain_openai import ChatOpenAI


class OpenaiAgent(Agent):
    _llm = ChatOpenAI(
        model=OPENAI_MODEL,
        api_key=os.getenv("OPENAI_API_KEY")
    )
