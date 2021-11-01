import requests


class Requests:
    def __init__(self):
        pass
        # self.url = str(url)

    def get(self, url):
        return requests.get(url)

    def post(self, url, payload):
        result = requests.post(
            str(url),
            json=dict(payload),
        )
        # print("STATUS CODE:", result.status_code)
        return result
