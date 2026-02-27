from crewai import Task

def budget_task(agent, budget):
    return Task(
        description=f"""
        You are the Budget Planner.

        Total budget: {budget}

        Use the research output to estimate costs.
        Be concise, realistic, and structured.

        Output Format (STRICT):

        Budget Breakdown:
        - Accommodation:
        - Food:
        - Transport:
        - Activities:
        --------------------------------
        Total:
        """,
        agent=agent,
        expected_output="str",
        markdown=True,
        output_file="output/budget_planner.md"
    )