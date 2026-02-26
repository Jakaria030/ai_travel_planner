from crewai import Crew
from llm.gemini_client import get_llm
from agents.researcher_agent import create_researcher
from tasks.researcher_task import research_task

def create_crew(data):

    researcher = create_researcher(get_llm())

    tasks = [
        research_task(researcher, data["destination"], data["preferences"]),
    ]

    return Crew(
        agents=[researcher],
        tasks=tasks,
        verbose=True
    )