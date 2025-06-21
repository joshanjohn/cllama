# Cllama [![Cllama Workflow](https://github.com/joshanjohn/cllama/actions/workflows/dependency-review.yml/badge.svg?branch=main)](https://github.com/joshanjohn/cllama/actions/workflows/dependency-review.yml)


Cllama is a python streamlit webUI for using LLM models which are available in the ollama localy. 



<img width="1295" alt="Screenshot 2025-06-21 at 19 30 28" src="https://github.com/user-attachments/assets/dec8d190-6208-4d5a-b19d-ec1f3aaf3f70" />
<img width="1295" alt="Screenshot 2025-06-21 at 20 08 04" src="https://github.com/user-attachments/assets/6548e738-b9ee-4ffd-bca5-0eb9e51a1577" />


# Installation Guide
1. ## Install Ollama locally:
   you can install using official doc https://ollama.com/download
   or you can run the `install_ollama.sh` bash file.Follow these commands:
  - `chmod +x install_ollama_models.sh`
  - `./install_ollama_models.sh`

2. ## Download a LLm model on Ollama
   Download any llm model's from the Ollama model Library https://ollama.com/search.
   for instance, to install IBM's Granite 3.3 model, use this command:
  - `ollama run granite3.3`
   To see the downloaded or available LLM models in the local Ollama, use this command:
  - `ollama list` 
   
3. ## Install UV dependency manager for python.
    use this command to install UV using python's pip
  - `pip install uv`
   use this command to install using Home Brew (recommended for Mac OS).
  - `brew install uv` 

4. ## Install cllama dependencies using UV.
  To sync all the dependencies for the cllama project, use 
  - `uv sync`

5. ## Runing cllama
  To run the cllama webUI project use this streamlit command from the base directory. 
- `streamlit run src/main.py`
