from crewai import Task

def validation_task(agent, budget, dates):
    return Task(
        description=f"""
        You are the Validation Agent.

        Validate outputs from:
        - Research
        - Budget
        - Itinerary

        Checks:
        1. Budget: Confirm total does not exceed {budget}.
        2. Research: Ensure all attractions exist.
        3. Schedule: Confirm itinerary fits within {dates}. Avoid overlaps.
        4. Risk & Assumptions: Identify any issues.

        Output Format (STRICT):

        Validation Summary:
        - Budget Status:
        - Assumptions:
        - Risk Factors:
        """,
        agent=agent,
        expected_output="str",
        markdown=True,
        output_file="output/validation.md"
    )