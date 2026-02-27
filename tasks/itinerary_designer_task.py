from crewai import Task

def itinerary_task(agent, dates, preferences):
    pref_text = f"Traveler Preferences: {', '.join(preferences)}" if preferences else ""

    return Task(
        description=f"""
        You are the Itinerary Designer.

        Trip Dates: {dates}
        {pref_text}

        Use only researched attractions. Avoid conflicts.  
        Include meals and realistic travel times.

        Output Format (STRICT):

        Day-wise Itinerary

        Day 1:
        - 09:00–11:00:
        - 12:00–13:00:
        - 14:00–17:00:
        - Evening:

        Day 2:
        ...

        End with:
        Estimated Daily Spending Pattern.
        """,
        agent=agent,
        expected_output="str",
        markdown=True,
        output_file="output/itinerary_designer.md"
    )