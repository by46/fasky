from  flask_mail import Message

from flasky import mail
from flasky.main import main


@main.route('/send_mail/<subject>', methods=['GET'])
def send_mail(subject):
    message = Message(subject=subject, sender='ycs_ctbu_2010@126.com', recipients=['ycs_ctbu_2010@126.com'])
    message.body = 'hello'
    mail.send(message)
    return "success"
