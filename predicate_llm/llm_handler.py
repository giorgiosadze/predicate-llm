import sys
from ollama import chat

def get_predicate_response(prompt, model="qwen2"):
    
    """
    Get a predicate response
    
    Args:
        prompt (str): The question to ask the LLM
        model (str): The model to use, defaults to qwen2
        
    Returns:
        str: Either "yes" or "no"
    """

    system_message = "only respond with a single word: either 'yes' or 'no'. No other text, explanation, or qualification is allowed in your response."
    
    messages = [
        {
            'role': 'system',
            'content': system_message,
        },
        {
            'role': 'user',
            'content': prompt,
        }
    ]
    
    try:
        response = chat(model, messages=messages)
        answer = response['message']['content'].strip().lower()
        
        if answer.startswith("yes"):
            return "yes"
        elif answer.startswith("no"):
            return "no"
        else:
            return "error"
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        return "error"
