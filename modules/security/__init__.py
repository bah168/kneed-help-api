# security/__init__.py
import warnings

from flask import url_for, redirect, Blueprint, flash
from sqlalchemy.exc import DatabaseError
from flask_admin import helpers
from flask_restful import Api
from flask_security import Security, SQLAlchemyUserDatastore, user_registered

from modules import admin, app
from modules.extensions import BaseModel
from .admin_views import ExtendedRegisterForm, ExtendedLoginForm
from .models import User
from modules.kneed_help.models.contact import ContactModel

security_bp = Blueprint('security_bp', __name__)
security_api = Api(security_bp)

"""
Manage User roles + tasks to secure resources
"""
user_datastore = SQLAlchemyUserDatastore(BaseModel, User, None)
security = Security(app, user_datastore,
                    login_form=ExtendedLoginForm,
                    register_form=ExtendedRegisterForm
                    )


@security.context_processor
def security_context_processor():
    return dict(
        admin_base_template=admin.base_template,
        admin_view=admin.index_view,
        h=helpers,
        get_url=url_for
    )


@app.before_first_request
def create_user():
    # Create the Admin user if not created
    if not User.find(1):
        user = user_datastore.create_user(
            username='admin',
            email='admin@email.com',
            password='password',
            first_name='Super',
            last_name='Admin'
        )
        user.session.commit()

@app.before_first_request
def create_contact():
    # Create the Admin user if not created
    if not ContactModel.find(1):
         ContactModel.create(
             email="<noreply@example.com>"
         )
         ContactModel.session.commit()


# set a newly registered user account to inactive and redirect to homepage
@user_registered.connect_via(app)
def user_registered_sighandler(app, user, confirm_token):
    user = User.query.filter(User.username == str(user)).first()
    if user:
        print(user)
        user.active = False
        try:
            user.session.commit()
        except DatabaseError:
            flash('An error occurred when creating account.')
        flash('Account has been created.')
        return redirect(url_for('admin.index'))



# Redirect app traffic to the modules default view
@app.route('/')
def no_endpoint_specified():
    return redirect(url_for('admin.index'))


""" Create models for module in dB """
with app.app_context():
    import modules.security.admin_views
    import modules.security.models

    # Register the admin views to the extension
    # Ignore warning messages from overridden fields
    with warnings.catch_warnings():
        warnings.filterwarnings('ignore', 'Fields missing from ruleset', UserWarning)
        admin.add_view(
            admin_views.UsersView(
                models.User,
                models.User.session,
                name='Users', category='Security'
            )
        )

app.register_blueprint(security_bp)

""" Register routes for modules """
import modules.security.routes
