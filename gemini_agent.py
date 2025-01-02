import os
from agent import Agent
from constants import GEMINI_MODEL
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI


genai.configure(api_key=os.environ['GOOGLE_API_KEY'])


class GeminiAgent(Agent):
    _llm = ChatGoogleGenerativeAI(model=GEMINI_MODEL)
