import local_settings

# URLS
URL_USER = "https://greencity-user.azurewebsites.net/ownSecurity/signIn"
URL_NEWS = "https://greencity.azurewebsites.net/econews/"
URL_UBS = "https://greencity-ubs.azurewebsites.net/"

# HEADERS


# PAYLOADS
CREDENTIALS = {"email": local_settings.EMAIL, "password": local_settings.PASSWORD}
BODY = {'addEcoNewsDtoRequest': '{"tags":["News"],"text":"asdasdasdasdasdasdasd","title":"Api Test News Postman","source":""}'}
# BODY = {'addEcoNewsDtoRequest': '{"tags":["News"],'
#                                 '"text":"Description for Test News",'
#                                 '"title":"Api Test News Postman",'
#                                 '"source":""}'}

try:
    from local_settings import *
except ImportError:
    pass
