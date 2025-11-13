import asyncio
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console

# Import custom modules
from src.tools import (
    delete_bq_table,
    delete_bq_dataset,
)
from src.config import (
    model_client,
)

class BigQueryAnalyst(AssistantAgent):
    """
    A BigQuery Analyst agent that gives summary and  usage insights into the BQ service of GCP account.
    """
    
    def __init__(self):
        super().__init__(
            name="big_query_analyst",
            model_client=model_client,
            tools=[delete_bq_table, delete_bq_dataset],
            # system_message=load_system_prompt("big_query_analyst_prompt.md"),
        )

        return

async def main():
    """
    Main function to run and test the Big Query Analyst.
    """
    
    # Instantiate the BigQuery Analyst Agent
    agent = BigQueryAnalyst()
    
    print("\n--- Chat Started ---")
    print("Type 'exit', 'quit', or 'terminate' to end the chat.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "terminate"]:
            break
        
        await Console(
            agent.run_stream(task=user_input),
        )
        
        
    return    

if __name__ == "__main__":
    asyncio.run(main())
