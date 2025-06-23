# 🤖Cllama [![Cllama Workflow](https://github.com/joshanjohn/cllama/actions/workflows/dependency-review.yml/badge.svg)](https://github.com/joshanjohn/cllama/actions/workflows/dependency-review.yml)


Cllama is a python streamlit webUI for using LLM models which are available in the ollama localy. 



<img width="1295" alt="Screenshot 2025-06-21 at 19 30 28" src="https://github.com/user-attachments/assets/dec8d190-6208-4d5a-b19d-ec1f3aaf3f70" />
<img width="1295" alt="Screenshot 2025-06-21 at 20 08 04" src="https://github.com/user-attachments/assets/6548e738-b9ee-4ffd-bca5-0eb9e51a1577" />


# Installation Guide
1. ## Install Ollama locally:
   you can install using official doc https://ollama.com/download
   or you can run the ```install_ollama.sh``` bash file.Follow these commands:
  - ```sh
    chmod +x install_ollama_models.sh```
    
  - ```sh
    ./install_ollama_models.sh```

2. ## Download a LLm model on Ollama
   Download any llm model's from the Ollama model Library https://ollama.com/search.
   for instance, to install IBM's Granite 3.3 model, use this command:
  - ```sh
    ollama run granite3.3```
   To see the downloaded or available LLM models in the local Ollama, use this command:
  - ```sh
    ollama list```
   
3. ## Install UV dependency manager for python.
    use this command to install UV using python's pip
  - ```sh
    pip install uv```
   use this command to install using Home Brew (recommended for Mac OS).
  - ```sh
    brew install uv```

4. ## Install cllama dependencies using UV.
  To sync all the dependencies for the cllama project, use 
  - ```sh
    uv sync```

5. ## Runing cllama
  To run the cllama webUI project use this streamlit command from the base directory. 
- ```sh
  streamlit run src/main.py```

# Contribution Guidelines
   a) Create a task in the project planning board (CPPB) https://github.com/users/joshanjohn/projects/17 <br>
   b) use proper branch name as github task suggest, which is hash number followed by task name seperated by hypen. (eg: 4-task-title) <br>
   c) Submit a pull request (PR) before merging into main branch. <br>
   d) Must get an PR approval review to merge. <br>

## Lint

1. In your terminal, `cd` into the project root
1. Run: `uv run ruff check`
1. To apply safe automatic fix, run: `uv run ruff check --fix`.
1. To apply unsafe automatic fix, run: `uv run ruff check --fix --unsafe-fixes`

__You may need to run formatter `black .` again after running ruff auto fix.__


## Format

1. In your terminal, `cd` into the project root
1. Run: `uv run black .`

**All The Best** 🙌🏻
