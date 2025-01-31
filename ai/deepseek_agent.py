import os
from ai.agent import Agent
from constants import DEEPSEEK_MODEL
from langchain_deepseek import ChatDeepSeek


class DeepseekAgent(Agent):
    _llm = ChatDeepSeek(
        model=DEEPSEEK_MODEL,
        api_key=os.getenv("DEEPSEEK_API_KEY")
    )
