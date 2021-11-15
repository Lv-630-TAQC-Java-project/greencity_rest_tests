import requests


class Requests:
    @staticmethod
    def get(url, headers):

        return requests.get(url, headers=headers)

    @staticmethod
    def post(url, headers, payload):
        result = requests.post(
            url,
            headers=headers,
            json=payload
        )
        return result
