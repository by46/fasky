from flask_wtf import Form
from wtforms import PasswordField
from wtforms import StringField
from wtforms import SubmitField
from wtforms import ValidationError
from wtforms.validators import DataRequired
from wtforms.validators import Email
from wtforms.validators import EqualTo
from wtforms.validators import Length
from wtforms.validators import Regexp

from flasky.models import User


class RegistrationForm(Form):
    email = StringField("Email", validators=[DataRequired(), Length(1, 64), Email()])
    username = StringField('Username', validators=[DataRequired(), Length(1, 64),
                                                   Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                                          'Username must have only letters, '
                                                          'numbers, dots or underscores')])

    password = PasswordField('Password', validators=[DataRequired(), Length(1, 16),
                                                     EqualTo('password2', "Password must match")])
    password2 = PasswordField('Password2', validators=[DataRequired(), Length(1, 16)])
    submit = SubmitField()

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError("Email already registered")

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError("Username already registered")
