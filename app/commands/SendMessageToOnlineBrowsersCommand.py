from cleo import Command
from pusher import Pusher


class SendMessageToOnlineBrowsersCommand(Command):
    """
    Sends a message to all currently online browsers

    send-messages-to-online-browsers
        {message : The text to send}
    """

    def handle(self):
        message = self.argument('message')

        pusher = Pusher(
            app_id='935879',
            key='c158052fb78ff1c7b4b2',
            secret='ab37b95e1648ba5c67cc',
            cluster='eu',
            ssl=True
        )

        pusher.trigger('my-channel', 'my-event', {'message': message})
