from crewai import Task


def validation_task(agent):
    return Task(
        description="""
        Validate:
        - Budget matches breakdown
        - Activities exist in researched data
        - No schedule conflicts
        - Identify risks and assumptions
        """,
        agent=agent,
        expected_output="str",
        markdown=True,
        output_file="output/validation.md"
    )