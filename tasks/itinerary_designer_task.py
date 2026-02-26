from crewai import Task


def itinerary_task(agent, dates):
    return Task(
        description=f"""
        Create a realistic day-wise itinerary for dates {dates}.
        Avoid overlapping times.
        """,
        agent=agent,
        expected_output="str",
        markdown=True,
        output_file="output/itinerary_designer.md"
    )
