from crewai import Task


def budget_task(agent, budget):
    return Task(
        description=f"""
        Create a detailed budget breakdown within {budget}.
        Include accommodation, food, transport, activities.
        Do not hallucinate unrealistic prices.
        """,
        agent=agent,
        expected_output="str",
        markdown=True,
        output_file="output/budget_planner.md"
    )