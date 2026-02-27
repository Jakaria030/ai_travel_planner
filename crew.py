from crewai import Crew
from llm.llm_model import get_llm
from agents.researcher_agent import create_researcher
from agents.budget_planner_agent import create_budget_planner
from agents.itinerary_designer_agent import create_itinerary_designer
from agents.validation_agent import create_validation
from tasks.researcher_task import research_task
from tasks.budget_planner_task import budget_task
from tasks.itinerary_designer_task import itinerary_task
from tasks.validation_task import validation_task


def create_crew(data):

    researcher = create_researcher(get_llm())
    budget_planner = create_budget_planner(get_llm())
    itinerary_designer = create_itinerary_designer(get_llm())
    validation = create_validation(get_llm())

    tasks = [
        research_task(researcher, data["destination"], data["preferences"]),
        budget_task(budget_planner, data["budget"]),
        itinerary_task(itinerary_designer, data["travel_dates"], data["preferences"]),
        validation_task(validation, data["budget"], data["travel_dates"])
    ]

    return Crew(
        agents=[researcher, budget_planner, itinerary_designer, validation],
        tasks=tasks,
        verbose=False
    )