from config.database import DB
from masonite.controllers import Controller
from masonite.request import Request
from masonite.response import Response
from masonite.validation import Validator
from masonite.view import View
from app.Subscription import Subscription
import feedparser
from app.jobs.DownloadEpisode import DownloadEpisode
from masonite import Queue
from os import path
import base64


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
        favorites = Subscription.where('favorite', True).get()
        subscriptions = Subscription.where('favorite', '!=', True).get()

        self.get_episodes(favorites)
        self.get_episodes(subscriptions)

        return view.render('podcasts.subscriptions', {
            'favorites': favorites,
            'subscriptions': subscriptions,
        })

    def get_episodes(self, podcasts):
        for podcast in podcasts:
            podcast.episodes = []

            for entry in feedparser.parse(podcast.url).entries:
                enclosure = next(
                    link for link in entry.links if link.rel == 'enclosure'
                )

                if (enclosure):
                    encodedBytes = base64.b64encode(
                        enclosure.href.encode("utf-8"))
                    name = str(encodedBytes, "utf-8")

                    is_downloaded = False

                    if path.exists('storage/episodes/' + name + '.mp3'):
                        is_downloaded = True

                    podcast.episodes.append({
                        'title': entry.title,
                        'enclosure': enclosure,
                        'is_downloaded': is_downloaded,
                    })

    def do_favorite(self, request: Request):
        # DB.table('subscriptions').where('id', request.param('id')).update({
        #     'favorite': True,
        # })

        subscription = Subscription.find(request.param('id'))
        subscription.favorite = True
        subscription.save()

        return request.redirect_to('podcasts-show-subscriptions')

    def do_unfavorite(self, request: Request):
        # DB.table('subscriptions').where('id', request.param('id')).update({
        #     'favorite': False,
        # })

        subscription = Subscription.find(request.param('id'))
        subscription.favorite = False
        subscription.save()

        return request.redirect_to('podcasts-show-subscriptions')

    def do_unsubscribe(self, request: Request):
        # DB.table('subscriptions').where('id', request.param('id')).delete()

        subscription = Subscription.find(request.param('id'))
        subscription.delete()

        return request.redirect_to('podcasts-show-subscriptions')

    def do_subscribe(self, request: Request):
        Subscription.create({
            'url': request.input('url'),
            'title': request.input('title'),
            'favorite': False,
        })

        return request.redirect_to('podcasts-show-subscriptions')

    def do_download(self, request: Request, queue: Queue):
        url = request.input('url')
        folder = 'storage/episodes'

        queue.push(DownloadEpisode(url, folder))

        return request.redirect_to('podcasts-show-subscriptions')
