import sys
import os

# Add the project root to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from workspace.src.orchestrator_agent import run_orchestrator

if __name__ == "__main__":
    if len(sys.argv) > 1:
        user_input = sys.argv[1]
        response = run_orchestrator(user_input)
        print(response)
    else:
        print("Error: No user input provided.")
        sys.exit(1)