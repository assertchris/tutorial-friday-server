"""Web Routes."""

from masonite.routes import Get, Post, Match

ROUTES = [
    Get().route('/', 'WelcomeController@show').name('welcome'),
    Match(['GET', 'POST'], '/home/@name', 'HomeController@show').name('home-with-name'),
    Match(['GET', 'POST'], '/home', 'HomeController@show').name('home-without-name'),
]
