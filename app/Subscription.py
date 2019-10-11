from config.database import Model


class Subscription(Model):
    __fillable__ = ['title', 'url', 'favorite']
