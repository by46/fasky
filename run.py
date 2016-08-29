"""deimos entry point

"""
import gevent.monkey

gevent.monkey.patch_all()

import os
from gevent.wsgi import WSGIServer

from flasky import create_app

if __name__ == '__main__':
    key = 'ENV'
    if key not in os.environ:
        os.environ[key] = 'development'

    config_name = os.environ.get(key)
    app = create_app(config_name)
    app.logger.info('flasky listening %s:%s', app.config['HTTP_HOST'], app.config['HTTP_PORT'])

    if os.environ.get('ENV', 'development') == 'development':
        app.run(app.config['HTTP_HOST'], app.config['HTTP_PORT'], debug=True)
    else:
        WSGIServer((app.config['HTTP_HOST'], app.config['HTTP_PORT']), application=app,
                   log=app.config['WSGI_LOG']).serve_forever()
