from masonite.routes import Get, Patch, Post, Match, RouteGroup

ROUTES = [
    Get('/', 'WelcomeController@show').name('welcome'),

    RouteGroup(
        [
            Match(['GET', 'POST'], '/@name',
                  'HomeController@show').name('with-name'),
            Match(['GET', 'POST'], '/',
                  'HomeController@show').name('without-name'),
        ],
        prefix='/home',
        name='home-',
    ),

    RouteGroup(
        [
            Get('/', 'PodcastController@show_search').name('-show-search'),
            Post('/', 'PodcastController@do_search').name('-do-search'),
            Get('/subscriptions',
                'PodcastController@show_subscriptions').name('-show-subscriptions'),
            Patch('/subscriptions/@id/favorite',
                  'PodcastController@do_favorite').name('-favorite-subscription'),
            Patch('/subscriptions/@id/unfavorite',
                  'PodcastController@do_unfavorite').name('-unfavorite-subscription'),
        ],
        prefix='/podcasts',
        name='podcasts',
    ),
]
