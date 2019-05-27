"""CSRF Middleware."""

from masonite.middleware import CsrfMiddleware as Middleware


class CsrfMiddleware(Middleware):
    """Verify CSRF Token Middleware."""

    exempt = [
        '/home',
        '/home/@name',
    ]

    every_request = False
    token_length = 30
