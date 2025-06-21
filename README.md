# Cllama
Cllama is a python streamlit webUI for using LLM models which are available in the ollama localy. 

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
