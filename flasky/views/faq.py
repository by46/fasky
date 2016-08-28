from flasky import app
from flasky import __version__


@app.route("/version", methods=['GET'])
def version():
    return __version__

@app.route("/faq.htm")
def faq():
    return "<!--Newegg-->"