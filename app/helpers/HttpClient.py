import requests

class HttpClient:
    def get(self, *args, **kwargs):
        return requests.get(*args, **kwargs)
