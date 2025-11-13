from autogen_agentchat.agents import AssistantAgent

# Import custom modules
from src.tools import (
    get_top_k_bq_users,
    get_top_k_bq_tables,
    delete_bq_table,
    delete_bq_dataset,
)
from src.config import (
    model_client,
)
from src.utils import load_system_prompt

class BigQueryAnalyst(AssistantAgent):
    """
    A BigQuery Analyst agent that gives summary and  usage insights into the BQ service of GCP account.
    """
    
    def __init__(self):
        super().__init__(
            name="big_query_analyst",
            model_client=model_client,
            tools=[get_top_k_bq_users, get_top_k_bq_tables, delete_bq_table, delete_bq_dataset],
            system_message=load_system_prompt("bigquery_analyst_prompt.md"),
        )

        return
