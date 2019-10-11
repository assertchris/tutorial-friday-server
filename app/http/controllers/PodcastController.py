from config.database import DB
from masonite.controllers import Controller
from masonite.request import Request
from masonite.validation import Validator
from masonite.view import View


class PodcastController(Controller):
    def __init__(self, request: Request):
        self.client = request.app().make('HttpClient')
        self.parser = request.app().make('RssParser')

    def show_search(self, view: View):
        return view.render('podcasts.search', {
            'podcasts': self.get_podcasts()
        })

    def get_podcasts(self, query=''):
        if query:
            response = self.client.get(
                'https://itunes.apple.com/search?media=podcast&term=' + query)
            return response.json()['results']

        return []

    def do_search(self, view: View, request: Request, validate: Validator):
        errors = request.validate(
            validate.required('terms')
        )

        if errors:
            request.session.flash('errors', errors)
            return request.back()

        return view.render('podcasts.search', {
            'podcasts': self.get_podcasts(
                request.input('terms')
            )
        })

    def show_subscriptions(self, view: View):
        subscriptions = DB.table('subscriptions').get()

        return view.render('podcasts.subscriptions', {
            'subscriptions': subscriptions,
        })
