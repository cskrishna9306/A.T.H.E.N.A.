from dotenv import load_dotenv
from autogen_ext.models.openai import OpenAIChatCompletionClient
from google.cloud import bigquery

# Load the environment variables from the .env file
load_dotenv()

# Define the BigQuery Region
BQ_REGION = "region-us"

# Define the BQ Project
BQ_PROJECT_ID = "scan-llms"

# Initialize the BQ client
bq_client = bigquery.Client(project=BQ_PROJECT_ID)

# The model to use
MODEL_NAME = "gpt-4o"

# The model client to use
model_client = OpenAIChatCompletionClient(
	model=MODEL_NAME,
)
