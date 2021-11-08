EMAIL = "user_email",
PASSWORD = "user_password"
BASE_URL_USER = "https://greencity-user.azurewebsites.net/ownSecurity/signIn"
BASE_URL_NEWS = "https://greencity.azurewebsites.net/"
BASE_URL_UBS = "https://greencity-ubs.azurewebsites.net/"
try:
    from local_settings import *
except ImportError:
    pass
