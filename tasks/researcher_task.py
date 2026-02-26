from crewai import Task


def research_task(agent, destination, preferences=None):
    pref_str = ""
    if preferences:
        pref_str = " Focus on these preferences: " + ", ".join(preferences) + "."

    return Task(
        description=f"""
        You are the Destination Researcher. Your goal is to generate a comprehensive destination overview for {destination}.{pref_str}. 
        Please provide the output in **Markdown format**. Use headings, bullet points, and formatting appropriately for Markdown.
        """,
        agent=agent,
        expected_output="str"
    )