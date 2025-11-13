import os
from dotenv import load_dotenv
from autogen_ext.models.openai import OpenAIChatCompletionClient

# Load the environment variables from the .env file
load_dotenv()

# Define the BigQuery Region
BQ_REGION = "region-us"

# Define the BQ Project
BQ_PROJECT_ID = "scan-llms"

# The model to use
MODEL_NAME = "gpt-4o"

# The model client to use
model_client = OpenAIChatCompletionClient(
	model=MODEL_NAME,
)

# config_list = [
#     {
#         "model": MODEL_NAME,
#         "api_key": os.environ.get("OPENAI_API_KEY"),
#     }
# ]
