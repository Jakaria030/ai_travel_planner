from crewai import Agent
from tools.serper_tool import serper_search
from utils.logger import logger


def create_researcher(llm):
    return Agent(
        role="Destination Researcher",
        goal="Find attractions, culture, travel info using live web search",
        backstory="Expert travel analyst using web search for real-time info.",
        tools=[serper_search],
        llm=llm,
        verbose=False,
    )