"""deimos entry point

"""
import gevent.monkey

gevent.monkey.patch_all()

import os
from gevent.wsgi import WSGIServer

from flasky import create_app

if __name__ == '__main__':
    app = create_app()
    print app.url_map
    app.logger.info('flasky listening %s:%s', app.config['HTTP_HOST'], app.config['HTTP_PORT'])

    if os.environ.get('ENV', 'development') == 'development':
        app.run(app.config['HTTP_HOST'], app.config['HTTP_PORT'], debug=True)
    else:
        WSGIServer((app.config['HTTP_HOST'], app.config['HTTP_PORT']), application=app,
                   log=app.config['WSGI_LOG']).serve_forever()
