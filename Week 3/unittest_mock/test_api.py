from unittest.mock import patch
from service import fetch_api_user


@patch("service.get_user_api")
def test_fetch_api_user(mock_api):

    mock_api.return_value = {
        "id": 1,
        "name": "Mock API User"
    }

    result = fetch_api_user()

    assert result["id"] == 1
    assert result["name"] == "Mock API User"

    mock_api.assert_called_once()