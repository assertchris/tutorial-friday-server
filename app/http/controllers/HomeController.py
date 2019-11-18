from masonite.auth import Auth
from masonite.request import Request
from masonite.view import View


class HomeController:

    def show(self, request: Request, view: View, auth: Auth):
        if not auth.user():
            request.redirect('/login')

        return view.render('home', {
            'name': request.param('name') or request.input('name'),
        })
