def test_get_api_token(post):
    respons = post
    assert 'accessToken' in respons, "Token is missing"

    print("\nToken is:", respons['accessToken'])

    assert len(respons['accessToken']) == 200, "Lenght of accessToken != 200"


def test_get_status_code(post):
    respons = post
    print("\nStatus Code:", respons.status_code)

    assert respons.status_code == 200, "Wrong Status Code, Must be 200"
