# security/views.py
import logging

from flask import flash
from wtforms.validators import DataRequired, Email, Optional
from modules.extensions import BaseView
from wtforms import StringField, PasswordField
from flask_security.utils import hash_password

logger = logging.getLogger("app")


class UsersView(BaseView):
    column_exclude_list = ('password',)
    form_excluded_columns = ('password', 'email')
    column_searchable_list = ('first_name', 'last_name', 'username')
    form_create_rules = ('email', 'first_name', 'last_name', 'username', 'set_password', 'active')
    form_edit_rules = ('email', 'first_name', 'last_name', 'username', 'update_password', 'active')
    form_extra_fields = dict(
        set_password=PasswordField("Password", validators=[DataRequired()]),
        update_password=PasswordField(
            "Password", render_kw={"placeholder": 'Enter new password here to change password'},
                validators=[Optional()]
        ),
        email=StringField('Email', validators=[Email()])
    )

    def on_model_change(self, form, model, is_created):

        if is_created:
            form.set_password.data = hash_password(form.set_password.data) #Hashes PasswordField before updating model
            model.update(password=form.set_password.data) #Updates UserModel
        else:
            if form.update_password.data:
                form.update_password.data = hash_password(form.update_password.data)
                model.update(password=form.update_password.data) #Admin Level Password change in UserModel

    def delete_model(self, model):
        if model.id == 1:
            flash("Cannot delete [ {} ] user.".format(model.name), category="warning")
            return False
        return super().delete_model(model)















