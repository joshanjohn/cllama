"""
Author: Joshan John
contact: joshanjohn2003@gmail.com
subjected to copyright@2025
"""

import pytest
from src.llm.llm import LLM
from langchain_ollama import ChatOllama


@pytest.fixture
def mock_chatollama(mocker):
    # Mock instance of ChatOllama
    mock_instance = mocker.Mock(spec=ChatOllama)
    mock_instance.invoke.return_value.content = "Mocked LLM response"
    mock_instance.get_name.return_value = "mock_model"

    # Patch ChatOllama in the LLM module path
    mocker.patch("src.llm.llm.ChatOllama", return_value=mock_instance)
    return mock_instance


def test_llm_initialization_with_valid_model(mock_chatollama):
    llm = LLM(model="llama2")
    assert isinstance(llm.llm, ChatOllama)
    mock_chatollama.get_name.assert_not_called()


def test_llm_initialization_without_model():
    with pytest.raises(ValueError, match="Model name is required to load ChatOllama."):
        LLM(model="")


def test_llm_run_with_valid_msg(mock_chatollama, capsys):
    llm = LLM(model="llama2")
    response = llm.run("Hello world")
    assert response == "Mocked LLM response"
    mock_chatollama.invoke.assert_called_once_with("Hello world")
    mock_chatollama.get_name.assert_called_once()
    captured = capsys.readouterr()
    assert "mock_model" in captured.out


def test_llm_run_with_empty_msg(mock_chatollama):
    llm = LLM(model="llama2")
    response = llm.run("")
    assert response == "Failed to generate LLM response"
    mock_chatollama.invoke.assert_not_called()
    mock_chatollama.get_name.assert_not_called()
