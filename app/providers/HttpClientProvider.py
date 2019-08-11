from masonite.provider import ServiceProvider
from app.helpers.HttpClient import HttpClient


class HttpClientProvider(ServiceProvider):
    wsgi = False

    def register(self):
        self.app.bind('HttpClient', HttpClient())

    def boot(self):
        pass
