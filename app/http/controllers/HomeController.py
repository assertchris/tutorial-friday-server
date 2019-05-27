"""A HomeController Module."""

from masonite.request import Request
from masonite.view import View

class HomeController:
    """HomeController Controller Class."""
    
    def __init__(self, request: Request):
        """HomeController Initializer
        
        Arguments:
            request {masonite.request.Request} -- The Masonite Request class.
        """
        self.request = request

    def show(self, view: View):
        return 'hello world'
