import asyncio
from autogen_agentchat.ui import Console

# Import custom modules
from src.bigquery_agent import BigQueryAnalyst

async def main():
    """
    Main function to run the Big Query Analyst.
    """
    
    # Instantiate the BigQuery Analyst Agent
    agent = BigQueryAnalyst()
    
    print("\n--- Chat Started ---")
    print("Type 'exit', 'quit', or 'terminate' to end the chat.\n")

    # Run the chat loop until the user exits
    while True:
        
        # Get user input
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "terminate"]:
            break
        
        # Run the agent and display the response stream
        await Console(
            agent.run_stream(task=user_input),
        )
        
    return    

if __name__ == "__main__":
    asyncio.run(main())

