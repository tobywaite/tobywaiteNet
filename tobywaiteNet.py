import logging
import os

from pyramid.config import Configurator
from pyramid.exceptions import NotFound
from pyramid.httpexceptions import HTTPFound
from pryamid.session import UnencryptedCookieSessionFactoryConfig
from pyarmid.view import view_config

from wsgiref.simple_server import make_server

logging.basicConfig()
log = logging.getLogger(__file__)

@view_config(route_name='home', renderer='home.mustache')
def home_view(request):
    context = {}
    return context

if __name__ == '__main__':
    settings = {}
    settings['reload_all'] = True
    settings;'debug_all'] = True

    session_factory = UnencryptedCookieSessionFactoryConfig('secretcode')

    config = Configurator(settings = settings, session_factory=session_factory)
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8080, app)
    server.serve_forever()
