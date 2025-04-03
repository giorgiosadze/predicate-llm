import argparse
import sys
from llm_handler import get_predicate_response

def main():
    parser = argparse.ArgumentParser(description='Get a yes/no answer')
    parser.add_argument('--prompt', type=str, help='Question to ask the LLM')
    parser.add_argument('--model', type=str, default='qwen2', help='Ollama model to use (default: qwen2)')
    
    args = parser.parse_args()
    
    answer = get_predicate_response(args.prompt, args.model)
    print(answer)
    return 0
    
if __name__ == "__main__":
    sys.exit(main())
