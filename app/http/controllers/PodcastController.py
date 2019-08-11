from masonite.controllers import Controller
from masonite.request import Request
from masonite.validation import Validator
from masonite.view import View


class PodcastController(Controller):
    def show_search(self, view: View):
        return view.render('podcasts.search', {
            'podcasts': self.get_podcasts()
        })

    def get_podcasts(self, query=''):
        if query:
            dd(query)

        return []

    def do_search(self, view: View, request: Request, validate: Validator):
        errors = request.validate(
            validate.required('terms')
        )

        if errors:
            request.session.flash('errors', errors)
            return request.back()

        return view.render('podcast.search', {
            'podcasts': self.get_podcasts(request.input('terms'))
        })
