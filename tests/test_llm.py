import pytest
from langchain_ollama import ChatOllama
from src.llm import LLM  # replace with actual module path


@pytest.fixture
def mock_chat_ollama(mocker):
    mock_instance = mocker.Mock(spec=ChatOllama)
    mock_instance.get_name.return_value = "mock-model"
    mock_instance.invoke.return_value.content = "mock-response"
    mocker.patch("src.llm.ChatOllama", return_value=mock_instance)
    return mock_instance


def test_init_loads_model(mock_chat_ollama):
    llm = LLM(model="my-model")
    assert isinstance(llm.llm, ChatOllama)
    assert llm.model == "my-model"
    mock_chat_ollama.get_name.assert_not_called()


def test_load_model_raises_on_empty_model():
    with pytest.raises(ValueError, match="Model name is required to load ChatOllama."):
        LLM(model="")


def test_run_returns_response(mock_chat_ollama, capsys):
    llm = LLM(model="my-model")
    result = llm.run("Hello")
    captured = capsys.readouterr()
    assert result == "mock-response"
    assert "mock-model" in captured.out
    mock_chat_ollama.invoke.assert_called_once_with("Hello")


def test_run_returns_failure_on_empty_msg(mock_chat_ollama):
    llm = LLM(model="my-model")
    result = llm.run("")
    assert result == "Failed to generate LLM response"
    mock_chat_ollama.invoke.assert_not_called()
