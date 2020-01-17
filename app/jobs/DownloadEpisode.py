from masonite.queues import Queueable
import base64
import requests


class DownloadEpisode(Queueable):
    def __init__(self, url, folder):
        self.url = url
        self.folder = folder

    def handle(self):
        encodedBytes = base64.b64encode(self.url.encode("utf-8"))
        name = str(encodedBytes, "utf-8")

        response = requests.get(self.url, stream=True)
        file = open(self.folder + '/' + name + '.mp3', 'wb')

        for chunk in response.iter_content(chunk_size=1024*1024):
            if chunk:
                file.write(chunk)
