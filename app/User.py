from config.database import Model
from masonite.auth import MustVerifyEmail


class User(Model, MustVerifyEmail):
    __fillable__ = ['name', 'email', 'password']
    __auth__ = 'email'
