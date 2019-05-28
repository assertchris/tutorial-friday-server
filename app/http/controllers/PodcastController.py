from masonite.view import View

class PodcastController:
    def show_search(self, view: View):
        return view.render('podcasts.search')
