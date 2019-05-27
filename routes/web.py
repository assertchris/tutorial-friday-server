"""Web Routes."""

from masonite.routes import Get, Match, RouteGroup

ROUTES = [
    Get().route('/', 'WelcomeController@show').name('welcome'),

    RouteGroup(
        [
            Match(['GET', 'POST'], '/@name', 'HomeController@show').name('with-name'),
            Match(['GET', 'POST'], '/', 'HomeController@show').name('without-name'),
        ],
        prefix = '/home',
        name = 'home-',
    )
]
