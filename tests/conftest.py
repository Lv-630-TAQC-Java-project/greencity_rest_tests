import json

import pytest as pytest

from setings import BASE_URL_USER, EMAIL, PASSWORD
from utils.api_client import Requests


@pytest.fixture()
def post():
    result = Requests().post(url=BASE_URL_USER,
                             payload={
                                 "email": EMAIL,
                                 "password": PASSWORD
                             })
    return json.loads(result.text)
