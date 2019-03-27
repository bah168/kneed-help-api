# modules/extensions/__init__.py
from flask_admin import Admin
from flask_cors import CORS
from flask_debugtoolbar import DebugToolbarExtension
from flask_mail import Mail
from flask_marshmallow import Marshmallow
from flask_restful import Api
from .database import get_session, init_db
from .base import BaseModel, BaseView, get_class_by_tablename

"""
Manage security roles/tasks
"""
admin = Admin(template_mode='bootstrap3', base_template="admin_layout.html")

"""
Handle requests
"""
cors = CORS()

"""
Handle emailing from the server
"""
mail = Mail()

# """
# dB API
# """
# db = SQLAlchemy(model_class=BaseModel)

# Make the session available to models in the DB
# BaseModel.set_session(db.session)

"""
Model serialization
"""
ma = Marshmallow()

"""
Backend API
"""
api = Api()

"""
Help debug routes
"""
route_debugger = DebugToolbarExtension()
