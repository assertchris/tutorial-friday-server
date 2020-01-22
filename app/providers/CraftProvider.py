from masonite.provider import ServiceProvider
from app.commands.SendMessageToOnlineBrowsersCommand import SendMessageToOnlineBrowsersCommand


class CraftProvider(ServiceProvider):
    wsgi = False

    def register(self):
        self.app.bind(
            'SendMessageToOnlineBrowsersCommand',
            SendMessageToOnlineBrowsersCommand()
        )

    def boot(self):
        pass
