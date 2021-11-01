from api_client import Requests
import json
from config import Credencials


result = Requests().post(url='https://greencity-user.azurewebsites.net/ownSecurity/signIn',
                             payload={
                                 "email": Credencials.user_email,
                                 "password": Credencials.user_password
                             })

token = json.loads(result.text)


def test_get_api_token():
    assert 'accessToken' in token, "Token is missing"

    print("\nToken is:", token['accessToken'])

    assert len(token['accessToken']) == 200, "Lenght of accessToken != 200"


def test_get_status_code():
    print("\nStatus Code:", result.status_code)

    assert result.status_code == 200, "Wrong Status Code, Must be 200"

