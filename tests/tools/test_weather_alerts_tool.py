import pytest
from unittest.mock import Mock
from src.tools.weather_alerts_tool import weather_alerts_tool
from src.constants import WEATHER_API_KEY, WEATHER_BASE_URL


@pytest.fixture
def mock_logger(mocker):
    """Patch the logger from src.utils."""
    return mocker.patch("src.tools.weather_alerts_tool.logger")


@pytest.fixture
def mock_requests_get(mocker):
    """Patch requests.get."""
    return mocker.patch("src.tools.weather_alerts_tool.requests.get")


def test_weather_alerts_tool_success(mock_logger, mock_requests_get):
    # Mock a successful API response
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "alerts": [{"title": "Storm warning"}]
    }
    mock_requests_get.return_value = mock_response

    query = "London"
    result = weather_alerts_tool.invoke(query)

    # Verify URL was constructed correctly
    expected_url = f"{WEATHER_BASE_URL}alerts.json?key={WEATHER_API_KEY}&q={query}"
    mock_logger.info.assert_any_call(f"URL = {expected_url}")
    mock_logger.info.assert_any_call(f"calling weather alerts api tool...")
    mock_logger.info.assert_any_call(f"fetched {query} weather information!")
    mock_logger.debug.assert_called_with(f"DATA = {mock_response.json.return_value['alerts']}")

    # Check returned data
    assert result == mock_response.json.return_value


def test_weather_alerts_tool_api_error(mock_logger, mock_requests_get):
    # Mock an API response with error
    mock_response = Mock()
    mock_response.status_code = 400
    mock_response.json.return_value = {"error": {"message": "Invalid location"}}
    mock_requests_get.return_value = mock_response

    query = "InvalidPlace"
    result = weather_alerts_tool.invoke(query)

    mock_logger.error.assert_called_with("400  - Invalid location")
    assert result == "No data find"


def test_weather_alerts_tool_empty_query():
    # Test that empty query raises ValueError
    with pytest.raises(ValueError, match="No place name provided to current weather api tool."):
        weather_alerts_tool.invoke("")


def test_weather_alerts_tool_requests_called_once(mock_logger, mock_requests_get):
    # Ensure requests.get is called exactly once
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"alerts": []}
    mock_requests_get.return_value = mock_response

    weather_alerts_tool.invoke("Paris")
    mock_requests_get.assert_called_once()
