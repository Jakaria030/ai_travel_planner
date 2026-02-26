from crewai import Agent

def create_itinerary_designer(llm):
    return Agent(
        role="Itinerary Designer",
        goal="Create optimized daily travel plans without time conflicts.",
        backstory="Professional travel scheduler.",
        llm=llm,
        verbose=False
    )