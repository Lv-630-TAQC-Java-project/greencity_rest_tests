import pytest as pytest

from setings import BASE_URL_USER, EMAIL, PASSWORD
from utils.api_client import Requests


@pytest.fixture()
def post():
    return Requests().post(url=BASE_URL_USER,
                           payload={
                               "email": EMAIL,
                               "password": PASSWORD
                           })
