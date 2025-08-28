import pytest
from unittest.mock import patch, Mock
from src.tools import current_weather_tool  # Replace 'your_module' with actual module name


class TestCurrentWeatherTool:
    """Test suite for current_weather_tool function"""

    @patch('src.tools.current_weather_tool.requests')  # Replace 'your_module' with actual module name
    @patch('src.tools.current_weather_tool.logger')
    def test_successful_weather_request(self, mock_logger, mock_requests):
        """Test successful weather API call"""
        # Arrange
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "location": {"name": "London"},
            "current": {"temp_c": 20, "condition": {"text": "Sunny"}}
        }
        mock_requests.get.return_value = mock_response
        
        # Act
        result = current_weather_tool.invoke("London")
        
        # Assert
        assert result == {
            "location": {"name": "London"},
            "current": {"temp_c": 20, "condition": {"text": "Sunny"}}
        }
        mock_requests.get.assert_called_once()
        mock_logger.info.assert_called()
        mock_logger.debug.assert_called_once()

    @patch('src.tools.current_weather_tool.requests')
    @patch('src.tools.current_weather_tool.logger')
    def test_api_error_response(self, mock_logger, mock_requests):
        """Test API error response handling"""
        # Arrange
        mock_response = Mock()
        mock_response.status_code = 400
        mock_response.json.return_value = {
            "error": {"message": "Invalid location"}
        }
        mock_requests.get.return_value = mock_response
        
        # Act
        result = current_weather_tool.invoke("InvalidPlace")
        
        # Assert
        assert result == "No data find"
        mock_logger.debug.assert_not_called()

    @patch('src.tools.current_weather_tool.requests')
    @patch('src.tools.current_weather_tool.logger')
    def test_api_server_error(self, mock_logger, mock_requests):
        """Test server error response"""
        # Arrange
        mock_response = Mock()
        mock_response.status_code = 500
        mock_response.json.return_value = {
            "error": {"message": "Internal server error"}
        }
        mock_requests.get.return_value = mock_response
        
        # Act
        result = current_weather_tool.invoke("London")
        
        # Assert
        assert result == "No data find"

    def test_empty_query_raises_value_error(self):
        """Test that empty query raises ValueError"""
        # Act & Assert
        with pytest.raises(ValueError, match="No place name provided to current weather api tool."):
            current_weather_tool.invoke("")
        
        with pytest.raises(ValueError):
            current_weather_tool.invoke(None)

    @patch('src.tools.current_weather_tool.requests')
    @patch('src.tools.current_weather_tool.logger')
    @patch('src.tools.current_weather_tool.WEATHER_BASE_URL', 'https://api.test.com/')
    @patch('src.tools.current_weather_tool.WEATHER_API_KEY', 'test_api_key')
    def test_correct_url_construction(self, mock_logger, mock_requests):
        """Test that URL is constructed correctly"""
        # Arrange
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"test": "data"}
        mock_requests.get.return_value = mock_response
        
        # Act
        current_weather_tool.invoke("Paris")
        
        # Assert
        expected_url = "https://api.test.com/current.json?key=test_api_key&q=Paris"
        mock_requests.get.assert_called_once_with(url=expected_url)
        mock_logger.info.assert_any_call(f"URL = {expected_url}")

    @patch('src.tools.current_weather_tool.requests')
    @patch('src.tools.current_weather_tool.logger')
    def test_logging_messages(self, mock_logger, mock_requests):
        """Test that appropriate log messages are called"""
        # Arrange
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"weather": "data"}
        mock_requests.get.return_value = mock_response
        query = "New York"
        
        # Act
        current_weather_tool.invoke(query)
        
        # Assert
        mock_logger.info.assert_any_call("calling current weather api tool...")
        mock_logger.info.assert_any_call(f"fetched {query} weather information!")

    @patch('src.tools.current_weather_tool.requests')
    @patch('src.tools.current_weather_tool.logger')
    def test_requests_exception_handling(self, mock_logger, mock_requests):
        """Test handling of requests exceptions"""
        # Arrange
        mock_requests.get.side_effect = Exception("Connection error")
        
        # Act & Assert
        with pytest.raises(Exception, match="Connection error"):
            current_weather_tool.invoke("London")

    @pytest.mark.parametrize("query,expected_in_url", [
        ("London", "q=London"),
        ("New York", "q=New York"),
        ("12345", "q=12345"),  # Postal code
        ("London, UK", "q=London, UK"),
    ])
    @patch('src.tools.current_weather_tool.requests')
    @patch('src.tools.current_weather_tool.logger')
    def test_various_query_formats(self, mock_logger, mock_requests, query, expected_in_url):
        """Test different query format handling"""
        # Arrange
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"test": "data"}
        mock_requests.get.return_value = mock_response
        
        # Act
        current_weather_tool.invoke(query)
        
        # Assert
        call_args = mock_requests.get.call_args
        assert expected_in_url in call_args.kwargs['url']


# Additional fixtures that might be useful
@pytest.fixture
def sample_weather_response():
    """Sample weather API response for testing"""
    return {
        "location": {
            "name": "London",
            "region": "City of London, Greater London",
            "country": "United Kingdom",
            "lat": 51.52,
            "lon": -0.11
        },
        "current": {
            "temp_c": 20.0,
            "temp_f": 68.0,
            "condition": {
                "text": "Partly cloudy",
                "icon": "//cdn.weatherapi.com/weather/64x64/day/116.png"
            },
            "humidity": 65,
            "wind_kph": 16.2
        }
    }


@pytest.fixture
def sample_error_response():
    """Sample error response from weather API"""
    return {
        "error": {
            "code": 1006,
            "message": "No matching location found."
        }
    }


# Integration-style test (if you want to test with actual constants)
class TestCurrentWeatherToolIntegration:
    """Integration tests using actual constants"""
    
    @patch('src.tools.current_weather_tool.requests')
    @patch('src.tools.current_weather_tool.logger')
    def test_with_actual_constants(self, mock_logger, mock_requests):
        """Test using actual WEATHER_BASE_URL and WEATHER_API_KEY constants"""
        # This test will use the actual imported constants
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"location": {"name": "London"}}
        mock_requests.get.return_value = mock_response
        
        result = current_weather_tool.invoke("London")
        
        assert "location" in result
        mock_requests.get.assert_called_once()
        # Verify the URL contains expected components
        call_url = mock_requests.get.call_args.kwargs['url']
        assert "current.json" in call_url
        assert "key=" in call_url
        assert "q=London" in call_url