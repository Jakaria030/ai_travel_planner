from crewai import Task

def research_task(agent, destination, preferences):
    pref_text = f"Traveler Preferences: {', '.join(preferences)}" if preferences else ""

    return Task(
        description=f"""
        You are the Destination Researcher.

        Destination: {destination}
        {pref_text}

        Do live web research. Include only real, verified information.  
        Be concise and structured.

        Output Format (STRICT):

        Travel Plan: {destination}

        ## Destination Overview
        - Best time to visit:
        - Culture summary:
        - Weather notes:
        - Entry requirements:

        ## Top Attractions
        List **max 5 attractions** (short description + estimated cost).

        ## Food & Dining
        - Local dishes:
        - Average meal cost:

        ## Transportation
        - Airport:
        - Local transport:
        - Avg daily transport cost:

        ## Estimated Daily Cost
        Provide realistic daily range.
        """,
        agent=agent,
        expected_output="str",
        markdown=True,
        output_file="output/destination_researcher.md"
    )