import requests


class Requests:
    def get(self, url):
        return requests.get(url)

    def post(self, url, payload):
        result = requests.post(
            str(url),
            json=dict(payload),
        )
        return result
