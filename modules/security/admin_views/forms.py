# security/forms.py
from flask_security.utils import hash_password
from flask_security.forms import LoginForm, RegisterForm
from wtforms import StringField, SelectMultipleField, TextField, PasswordField
from wtforms.validators import InputRequired


class ExtendedLoginForm(LoginForm):
    email = StringField('Username or email', [InputRequired()])


class ExtendedRegisterForm(RegisterForm):
    username = StringField('Username', [InputRequired()])
    first_name = StringField('First Name', [InputRequired()])
    last_name = StringField('Last Name', [InputRequired()])








