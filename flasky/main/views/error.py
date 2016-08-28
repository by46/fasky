import httplib

from flask import render_template

from flasky.main import main


@main.errorhandler(httplib.NOT_FOUND)
def page_not_found(ex):
    return render_template('404.html'), httplib.NOT_FOUND
