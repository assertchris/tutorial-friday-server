from masonite.view import View


class HomeController:

    def show(self, view: View):
        # if not auth.user():
        #     request.redirect('/login')

        return view.render('home', {
            'name': request().param('name') or auth().email,
        })
