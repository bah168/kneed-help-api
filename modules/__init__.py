# modules/__init__.py
from flask import Flask

from modules.extensions import (
    admin, api, cors, mail, route_debugger,
    ma, init_db, get_session, BaseModel
)

""" Startup Configuration """
app = Flask(
    __name__,
    template_folder='../templates',
    static_folder='../static'
)

"""
Initialize module configuration
Loads the settings for extensions
"""
import modules.config

# DB
engine, session = get_session(app)
BaseModel.set_session(session)

"""
Configure security for the application
"""
import modules.security

# JWT Resource Authentication

""" Module Registration """
import modules.kneed_help


init_db(app, engine, session)

"""
Bind the application context to our extensions
"""
admin.init_app(app)
api.init_app(app)                               # Manage application routes
cors.init_app(app, supports_credentials=True)   # Handle cross realm traffic
ma.init_app(app)                                # Serialization for app models
mail.init_app(app)                              # Manage mailing server
#route_debugger.init_app(app)                    # Browser based debug information
