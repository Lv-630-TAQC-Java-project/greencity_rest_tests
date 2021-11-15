import pytest as pytest
import json

from settings import *
from utils.api_client import Requests


@pytest.fixture
def post_get_token():
    result = Requests().post(url=URL_USER,
                             headers='',
                             payload=CREDENTIALS)
    token = json.loads(result.text)
    return token['accessToken']


@pytest.fixture
def post_get_status_code():
    result = Requests().post(url=URL_USER,
                             headers='',
                             payload=CREDENTIALS)
    return result.status_code


@pytest.fixture
def post_create_news(post_get_token):
    headers = {'Accept': '*/*',
               'Authorization': f'Bearer {post_get_token}',
               'Content-Type': 'multipart/form-data'}
    result = Requests().post(
        url=URL_NEWS,
        headers=headers,
        payload=BODY)
    return result.status_code


@pytest.fixture
def get_user_info(post_get_token):
    headers = {'accept': '*/*',
               "Authorization": f"Bearer {post_get_token}"}
    result = Requests().get(url='https://greencity-user.azurewebsites.net/user',
                            headers=headers
                            )
    return result.status_code
