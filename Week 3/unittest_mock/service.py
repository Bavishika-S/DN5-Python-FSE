from database import get_user_from_db
from api import get_user_api


def fetch_user(user_id):
    return get_user_from_db(user_id)


def fetch_api_user():
    return get_user_api()
