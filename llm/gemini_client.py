import os
from dotenv import load_dotenv
from crewai import LLM

load_dotenv()

# Read configuration from environment
MODEL = os.getenv("GEMINI_MODEL", "gemini/gemini-2.0-flash")
API_KEY = os.getenv("GEMINI_API_KEY")
TEMPERATURE = float(os.getenv("GEMINI_TEMPERATURE", 0.7))

def get_llm():
    return LLM(
        model=MODEL,
        api_key=API_KEY,
        temperature=TEMPERATURE
    )
