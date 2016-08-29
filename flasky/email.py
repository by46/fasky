from flask import current_app
from flask import render_template
from flask_mail import Message

from flasky import mail


def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


def send_mail(to, subject, template, **kwargs):
    message = Message(subject=current_app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + subject,
                      sender=current_app.config['FLASKY_MAIL_SENDER'],
                      recipients=[to])
    message.body = render_template(template + '.txt', **kwargs)
    message.html = render_template(template + '.html', **kwargs)
    # worker = Thread(target=send_async_email, args=[current_app, message])
    # worker.start()
    mail.send(message)
    return True
