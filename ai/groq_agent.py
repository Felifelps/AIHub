import os
from ai.agent import Agent
from constants import GROQ_MODEL
from langchain_groq import ChatGroq


class GroqAgent(Agent):
    _llm = ChatGroq(
        model=GROQ_MODEL,
        api_key=os.getenv("GROQ_API_KEY")
    )
