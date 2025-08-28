import pytest
from src.llm.llm import LLM  # import the actual module containing the class


@pytest.fixture
def mock_chatollama(mocker):
    return mocker.patch("src.llm.llm.ChatOllama")


@pytest.fixture
def mock_logger(mocker):
    return mocker.patch("src.llm.llm.logger")


def test_get_llm_model_with_model_returns_chatollama(mock_chatollama, mock_logger):
    llm_instance = LLM(model="test-model")
    result = llm_instance.get_llm_model()
    mock_logger.info.assert_called_once_with("LLM = test-model")
    mock_chatollama.assert_called_once_with(model="test-model")
    assert result == mock_chatollama.return_value


def test_get_llm_model_without_model_raises(mock_logger):
    llm_instance = LLM(model="")
    with pytest.raises(ValueError):
        llm_instance.get_llm_model()
    mock_logger.error.assert_called_once_with(
        "Model name is required to load ChatOllama."
    )


def test_call_with_empty_message_returns_error(mock_logger):
    llm_instance = LLM(model="test-model")
    result = llm_instance("")
    assert result == "Failed to generate LLM response"
    mock_logger.error.assert_called_once_with("Failed to generate LLM response")


def test_call_with_valid_message(mock_chatollama, mock_logger):
    mock_instance = mock_chatollama.return_value
    mock_instance.invoke.return_value.content = "response"
    mock_instance.get_name.return_value = "test-model"

    llm_instance = LLM(model="test-model")
    result = llm_instance("Hello")

    mock_chatollama.assert_called_once_with(model="test-model")
    mock_logger.debug.assert_called_once_with("Model test-model loaded ... ")
    assert result == "response"
