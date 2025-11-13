from pathlib import Path
from functools import cache

@cache
def load_system_prompt(promptFile: str) -> str | None:
    """
    Load the system prompt from the given file.

    Args:
        promptFile: The name of the prompt file to load

    Returns:
        The system prompt from the given file
    """
    
    # Load the system prompt from the given file
    try:
        prompt_path = Path(__file__).parent.parent / "prompts" / promptFile
        return prompt_path.read_text(encoding="utf-8")
    except FileNotFoundError as e:
        print(f"Error: Prompt file {promptFile} not found: {e}")
    except Exception as e:
        print(f"Error loading prompt file {promptFile}: {e}")
    
    return None