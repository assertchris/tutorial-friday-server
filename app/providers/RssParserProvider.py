from masonite.provider import ServiceProvider
from app.helpers.RssParser import RssParser


class RssParserProvider(ServiceProvider):
    wsgi = False

    def register(self):
        self.app.bind('RssParser', RssParser())

    def boot(self):
        pass
