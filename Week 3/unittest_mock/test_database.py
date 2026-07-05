from unittest.mock import patch
from service import fetch_user


@patch("service.get_user_from_db")
def test_fetch_user(mock_db):

    mock_db.return_value = {
        "id": 1,
        "name": "Mock User"
    }

    result = fetch_user(1)

    assert result["id"] == 1
    assert result["name"] == "Mock User"

    mock_db.assert_called_once_with(1)