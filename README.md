# AI Travel Planner

An intelligent travel planning system using **CrewAI multi-agent architecture**. The system generates complete travel plans, including destination research, budget estimation, day-wise itinerary, and validation, using real-time web search and structured LLM outputs.

---

## Features

- **Destination Research:** Finds attractions, cultural highlights, transportation info, and food recommendations using live web search (Serper API).  
- **Budget Planner:** Estimates accommodation, food, transport, and activities based on real data.  
- **Itinerary Designer:** Creates a realistic, conflict-free daily travel plan.  
- **Validation Agent:** Verifies feasibility, budget consistency, and logical correctness of the travel plan.  
- **Structured Output:** Markdown files for each agent output; ready for further processing or display.  

---

## Getting Started
Follow these steps to set up and run the project locally:

1. Clone the repository:
    ```bash
    git clone git@github.com:Jakaria030/ai_travel_planner.git
    ```
2. Navigate to the project directory:
    ```bash
    cd ai_travel_planner
    ```
3. Create Virtual Environment
    ```bash
    uv venv
    ```
4. Activate Virtual Environment
    ```bash
    source .vevn/bin/activate
    ```
5. Install Dependencies
    ```bash
    pip install -r requirements.txt
    ```
6. Create a `.env` file in the project root with the following variables:
    ```env
    MODEL=<ai model>
    API_KEY=<ai api key>
    TEMPERATURE=<temperature number like 0.3>
    SERPER_API_KEY=<serper api key>
    SERPER_SEARCH_URL=<serper search url>
    ```
7. Run the project
    ```bash
    uv run main.py --destination Bangladesh --dates "2026-02-27 to 2026-02-28" --budget 10000 --preferences "Cox Bazar, Chattagram"
    ```

## Script Arguments

| Argument       | Required / Optional | Description                                                              | Example                            |
|----------------|---------------------|--------------------------------------------------------------------------|------------------------------------|
| `--destination`| Required            | The country or city you want to plan the trip for.                       | `Bangladesh`                       |
| `--dates`      | Required            | Trip start and end dates in `"YYYY-MM-DD to YYYY-MM-DD"` format.         | `"2026-02-27 to 2026-02-28"`       |
| `--budget`     | Required            | Total budget for the trip (used by Budget Planner and Validation Agent). | `10000`                            |
| `--preferences`| Optional            | Traveler-specific interests or places to prioritize (comma-separated).   | `"Cox Bazar, Chattagram"`          |


## Analysis Section


**Why Multi-Agent?**

- **Separation of Concerns:** Each agent specializes in a single responsibility (research, budgeting, itinerary, validation), making the system modular and maintainable.
- **Parallel Reasoning:** Multi-agent flow allows structured handoff of outputs between agents, ensuring each stage gets only relevant information.
- **Scalability:** Agents can be replaced or upgraded independently, e.g., swapping LLMs or adding more validation checks.


## What If Serper Returns Incorrect Data?

- Agents downstream (Budget, Itinerary, Validation) rely on structured research output.
- Mitigation: Validation Agent checks for inconsistencies; agents are instructed to only use verified sources.
- Optionally, a confidence score or fact-checking module can be added for high-risk decisions.


## What If Budget Is Unrealistic?

- Budget Planner uses realistic price ranges and capped estimates.
- Validation Agent flags outputs exceeding user-provided or plausible budgets.
- Mitigation: Include constraints and fallback defaults to prevent nonsensical cost outputs.


## Hallucination Risks

- LLMs may generate fake attractions, food items, or transport info.
- Mitigation strategies:
    - Research agent must only include verifiable information.
    - Validation agent checks for consistency between sections.
    - Output is constrained by structured format and token limits to reduce verbosity.


## Token Usage

- Multi-agent setup increases token usage because each agent may receive large context from previous outputs.
- Mitigation:
    - Limit number of attractions (max 5).
    - Summarize outputs before passing to downstream agents.
    - Optional: automatic retries for rate-limited API calls.


## Scalability
- Horizontal: Can add new agents (e.g., hotel booking, local events) without breaking existing pipeline.
- Vertical: Each agent’s LLM call can scale independently based on token budget and API throughput.
- Structured outputs allow integration with web frontends or dashboards without rewriting agent logic.


## Additional Resources
- [Python Documentation](https://docs.python.org/3/)
- [CrewAI Documentation](https://docs.crewai.com/en/introduction)