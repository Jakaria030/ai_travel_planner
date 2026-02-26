from crewai import Crew
from llm.llm_model import get_llm
from agents.researcher_agent import create_researcher
from agents.budget_planner_agent import create_budget_planner
from tasks.researcher_task import research_task
from tasks.budget_planner_task import budget_task

def create_crew(data):

    researcher = create_researcher(get_llm())
    budget_planner = create_budget_planner(get_llm())

    tasks = [
        research_task(researcher, data["destination"], data["preferences"]),
        budget_task(budget_planner, data["budget"])
    ]

    return Crew(
        agents=[researcher, budget_planner],
        tasks=tasks,
        verbose=False
    )