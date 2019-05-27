"""Web Routes."""

from masonite.routes import Get, Post

ROUTES = [
    Get().route('/', 'WelcomeController@show').name('welcome'),
    Get().route('/home/@name', 'HomeController@show').name('home'),
    Get().route('/home', 'HomeController@show').name('home'),
]
