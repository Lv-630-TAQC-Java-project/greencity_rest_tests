def test_get_api_token(post):
    import json
    response = json.loads(post.text)
    assert 'accessToken' in response, "Token is missing"

# //only for presentation
    print("\nToken is:", response['accessToken'])

    assert len(response['accessToken']) == 200, "Lenght of accessToken != 200"


def test_get_status_code(post):
    response = post.status_code

    # only for presentation
    print("\nStatus Code:", response)

    assert response == 200, "Wrong Status Code, Must be 200"
