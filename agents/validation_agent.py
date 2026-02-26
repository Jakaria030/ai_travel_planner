from crewai import Agent

def create_validation(llm):
    return Agent(
        role="Validation Agent",
        goal="Verify feasibility, budget consistency, and logical errors.",
        backstory="Audit specialist ensuring realistic travel plans.",
        llm=llm,
        verbose=False
    )