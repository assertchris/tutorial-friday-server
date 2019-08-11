"""Web Routes."""

from masonite.routes import Get, Post, Match, RouteGroup

ROUTES = [
    Get('/', 'WelcomeController@show').name('welcome'),

    RouteGroup(
        [
            Match(['GET', 'POST'], '/@name', 'HomeController@show').name('with-name'),
            Match(['GET', 'POST'], '/', 'HomeController@show').name('without-name'),
        ],
        prefix = '/home',
        name = 'home-',
    ),

    RouteGroup(
        [
            Get('/', 'PodcastController@show_search').name('-show-search'),
            Post('/', 'PodcastController@do_search').name('-do-search')
        ],
        prefix = '/podcasts',
        name = 'podcasts',
    ),
]
