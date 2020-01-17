from masonite.routes import Delete, Get, Patch, Post, Match, RouteGroup

ROUTES = [
    Get('/', 'WelcomeController@show').name('welcome'),

    RouteGroup(
        [
            Match(['GET', 'POST'], '/@name',
                  'HomeController@show').name('with-name'),
            # Match(['GET', 'POST'], '/',
            #       'HomeController@show').name('without-name'),
        ],
        prefix='/home',
        name='home-',
        middleware=['auth', 'verified'],
    ),

    Match(['GET', 'POST'], '/home',
          'HomeController@show').name('without-name').middleware('auth', 'verified'),

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
            Delete('/subscriptions/@id/unsubscribe',
                   'PodcastController@do_unsubscribe').name('-unsubscribe'),
            Post('/subscribe', 'PodcastController@do_subscribe').name('-subscribe'),
            Post('/download', 'PodcastController@do_download').name('-download'),
        ],
        prefix='/podcasts',
        name='podcasts',
    ),
]

ROUTES = ROUTES + [
    Get().route('/login', 'LoginController@show').name('login'),
    Get().route('/logout', 'LoginController@logout').name('logout'),
    Post().route('/login', 'LoginController@store'),
    Get().route('/register', 'RegisterController@show').name('register'),
    Post().route('/register', 'RegisterController@store'),
    # Get().route('/home', 'HomeController@show').name('home'),
    Get().route('/email/verify', 'ConfirmController@verify_show').name('verify'),
    Get().route('/email/verify/send', 'ConfirmController@send_verify_email'),
    Get().route('/email/verify/@id:signed', 'ConfirmController@confirm_email'),
    Get().route('/password', 'PasswordController@forget').name('forgot.password'),
    Post().route('/password', 'PasswordController@send'),
    Get().route('/password/@token/reset',
                'PasswordController@reset').name('password.reset'),
    Post().route('/password/@token/reset', 'PasswordController@update'),
]
