# A.T.H.E.N.A.

Automated Tracking &amp; Heuristic Engine for Networked Assets

## Prerequisites

- Google BigQuery access (service account recommended)
- OpenAI API access (for Autogen models)

## Installation

1. Create and activate a virtual environment (replace `.venv` with your preferred path):

   ```
   python -m venv .venv
   source .venv/bin/activate
   ```

2. Install the project in editable mode so the agent code can be modified without reinstalling:

   ```
   pip install -e .
   ```

## Configuration

Create a `.env` file in the repository root with the credentials required by the agent:

- `OPENAI_API_KEY` – API key used by `autogen-ext` to talk to the OpenAI-compatible endpoint.
- `GOOGLE_APPLICATION_CREDENTIALS` – absolute path to the Google Cloud service-account JSON file used for BigQuery.

Ensure the referenced service account has permission to query the BigQuery project configured in `src/config.py`.

## Running the BigQuery Analyst

Start the console chat interface with:

```
python -m src.main
```

After the banner appears you can begin asking questions such as “What is the table with the biggest size?” and the agent will respond using live BigQuery data.
