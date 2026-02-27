import argparse
from utils.logger import logger
from crew import create_crew


def parse_arguments():
    parser = argparse.ArgumentParser(description="Multi-Agent AI Travel Planner")

    parser.add_argument(
        "--destination",
        type=str,
        required=True,
        help="Travel destination"
    )

    parser.add_argument(
        "--dates",
        type=str,
        required=True,
        help="Travel dates (YYYY-MM-DD to YYYY-MM-DD)"
    )

    parser.add_argument(
        "--budget",
        type=float,
        required=True,
        help="Total travel budget"
    )

    parser.add_argument(
        "--preferences",
        type=str,
        required=False,
        default="",
        help="Comma-separated preferences (Optional)"
    )

    return parser.parse_args()


def main():
    logger.info("Starting AI Travel Planner...")

    arguments = parse_arguments()
    user_input = {
        "destination": arguments.destination,
        "travel_dates": arguments.dates,
        "budget": arguments.budget,
        "preferences": (
            [p.strip() for p in arguments.preferences.split(",")]
            if arguments.preferences else []
        )
    }

    create_crew(user_input).kickoff()

    # Read all task
    with open("output/destination_researcher.md") as f:
        print(f.read())

    with open("output/budget_planner.md") as f:
        print(f.read())

    with open("output/itinerary_designer.md") as f:
        print(f.read())

    with open("output/validation.md") as f:
        print(f.read())

    logger.info("AI Travel Planner Execution Completed.")


if __name__ == "__main__":
    main()
