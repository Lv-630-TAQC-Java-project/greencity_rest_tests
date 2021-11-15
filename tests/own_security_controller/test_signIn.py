

def test_get_api_token(post_get_token):
    assert post_get_token, "Length of accessToken != 200"


def test_get_status_code(post_get_status_code):
    assert post_get_status_code == 200, "Wrong Status Code, Must be 200"


def test_create_news(post_create_news):
    assert post_create_news == 201


def test_get_user_info(get_user_info):
    assert get_user_info == 200
