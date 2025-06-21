#!/bin/bash

set -e

echo "🔍 Checking if Ollama is installed..."

if ! command -v ollama &> /dev/null; then
    echo "📦 Ollama not found. Installing..."

    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        curl -fsSL https://ollama.com/install.sh | sh
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        brew install ollama
    else
        echo "❌ Unsupported OS: $OSTYPE"
        exit 1
    fi

    echo "✅ Ollama installed."
else
    echo "✅ Ollama is already installed."
fi

# Start Ollama service in background
echo "🚀 Ensuring Ollama service is running..."
pgrep -f "ollama serve" > /dev/null || {
    nohup ollama serve > /dev/null 2>&1 &
    sleep 5
    echo "✅ Ollama service started."
}

# Check if model is already pulled
check_and_pull_model() {
    MODEL_NAME=$1
    if ollama list | grep -q "^$MODEL_NAME"; then
        echo "✅ Model '$MODEL_NAME' is already installed."
    else
        echo "📥 Pulling model '$MODEL_NAME'..."
        ollama pull "$MODEL_NAME"
        echo "✅ Model '$MODEL_NAME' installed."
    fi
}

# Install Granite and LLaMA3 models
check_and_pull_model "granite"
check_and_pull_model "llama3"

echo "📋 Final model list:"
ollama list
