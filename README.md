# Predicate LLM

A simple AI powered command-line tool that returns "yes" or "no" answers from a local LLM using Ollama.

## Prerequisites

- Python 3.7+
- [Ollama](https://ollama.ai/) installed and running locally
- qwen2 model pulled in Ollama (or another model of your choice)

## Installation

```bash
# Clone the repository
git clone https://github.com/giorgiosadze/predicate-llm.git
cd predicate-llm

# Install the package
pip install -e .
```

## Usage

```bash
# Basic usage (uses qwen2 model by default)
python cli.py --prompt "Is C++ a computer"
# Output: no

# Using a different model
python cli.py --model "gemma3:latest" --prompt "Is C++ a computer language"
# Output: yes
```

## License

MIT
