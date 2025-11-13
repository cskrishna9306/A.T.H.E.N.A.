import autogen
import os
import asyncio
from dotenv import load_dotenv
from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_agentchat.ui import Console

load_dotenv()
# 💡 Step 1: Configuration 
# Load your LLM configuration. This assumes you have an OAI_CONFIG_LIST
# environment variable or a configuration file.
# You can also set it directly:
# config_list = [
#     {
#         "model": "gpt-3.5-turbo",  # Or any other model
#         "api_key": os.environ.get("OPENAI_API_KEY"),
#     }
# ]

# A common way to load config is from a JSON file or env var
try:
    config_list = autogen.config_list_openai_aoai(
        key_filter={"model": ["gpt-3.5-turbo", "gpt-4"]},
    )
except Exception:
    print("Warning: Failed to load config from autogen.config_list_openai_aoai. Using a placeholder.")
    # Placeholder for running without a valid config setup (replace with your actual config)
    config_list = [{"model": "gpt-3.5-turbo", "api_key": os.environ.get("OPENAI_API_KEY")}]
    # Note: The script will fail unless you replace "YOUR_FAKE_KEY" 
    # and have a valid config setup.

async def main():
    # llm_config = {"config_list": config_list}
    model_client = OpenAIChatCompletionClient(
        model="gpt-4o",
    )
    # ---
    ## 🤖 Agent Setup
    # ---

    # The AssistantAgent is the chatbot that will use the LLM to generate responses.
    assistant = AssistantAgent(
        name="ChatBot",
        model_client=model_client,
        system_message="You are a helpful and friendly general-purpose chatbot. Keep your responses concise.",
    )

    # The UserProxyAgent represents the human user.
    # The 'human_input_mode="ALWAYS"' is crucial: it makes the agent always ask for 
    # human input after a turn, facilitating the back-and-forth.
    # 'is_termination_msg' checks if the user's message is a termination command.
    # user_proxy = autogen.UserProxyAgent(
    #     name="User",
    #     human_input_mode="ALWAYS",  # This enables the interactive chat loop
    #     max_consecutive_auto_reply=0, # Prevents the user_proxy from auto-replying
    #     is_termination_msg=lambda x: x.get("content", "").lower() in ["exit", "quit", "terminate"],
    #     code_execution_config=False, # Disable code execution for a simple chatbot
    # )

    # ---
    ## 💬 Initiate Conversation
    # ---

    # The initiate_chat function starts the conversation.
    # The `message` is the first prompt sent to the AssistantAgent.
    # The conversation will continue until the user types one of the termination messages.

    print("\n--- Chat Started ---")
    print("Type 'exit', 'quit', or 'terminate' to end the chat.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "terminate"]:
            break
        # result = await assistant.run(task=user_input)
        # print(result.messages)
        await Console(
            assistant.run_stream(task=user_input),
            # output_stats=True,  # Enable stats printing.
        )

    # result = await assistant.run(task="Find information on AutoGen")
    # print(result.messages)
    # user_proxy.initiate_chat(
    #     assistant,
    #     message="Hello! I'm here to chat. What's on your mind today?",
    #     # The default max_turns is 10, which is often enough for a chatbot. 
    #     # If you want a virtually infinite conversation, you could set a very high number.
    #     # max_turns=1000 
    # )

    print("\n--- Chat Ended ---")
    

if __name__ == "__main__":
    asyncio.run(main())