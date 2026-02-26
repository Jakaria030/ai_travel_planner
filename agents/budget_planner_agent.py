from crewai import Agent

def create_budget_planner(llm):
    return Agent(
        role="Budget Planner",
        goal="Estimate realistic costs using researched data",
        backstory="Financial travel expert specializing in cost breakdowns.",
        llm=llm,
        verbose=False,
    )