"""A HomeController Module."""

from masonite.request import Request
from masonite.view import View

class HomeController:
    """HomeController Controller Class."""

    def show(self, view: View, request: Request):
        return 'hello ' + (request.param('name') or request.input('name'))
