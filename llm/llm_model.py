import os
from dotenv import load_dotenv
from crewai import LLM

load_dotenv()

# Read configuration from environment
MODEL = os.getenv("MODEL")
API_KEY = os.getenv("API_KEY")
TEMPERATURE = float(os.getenv("TEMPERATURE"))

def get_llm():
    return LLM(
        model=MODEL,
        api_key=API_KEY,
        temperature=TEMPERATURE
    )
