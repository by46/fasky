from flasky.main import main


@main.route("/version", methods=['GET'])
def version():
    return '0.0.1'


@main.route("/faq.htm")
def faq():
    return "<!--Newegg-->"
