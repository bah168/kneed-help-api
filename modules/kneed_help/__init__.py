# inventory/__init__.py
import os
from modules import app
from flask import Blueprint
from flask_restful import Api
from modules.extensions import admin


kneed_help_bp = Blueprint('kneed_help_bp', __name__)
kneed_help_api = Api(kneed_help_bp)


""" Create models for module in dB """
with app.app_context():
    import modules.kneed_help.admin_views
    import modules.kneed_help.models

    admin.add_view(
        admin_views.BodyPartsView(
            models.PartOfBodyModel,
            models.PartOfBodyModel.session,
            name='Body Parts', category='Body'
        )
    )
    admin.add_view(
        admin_views.BodySubpartsView(
            models.SubpartsModel,
            models.SubpartsModel.session,
            name='Body Subparts', category='Body'
        )
    )
    admin.add_view(
        admin_views.ConditionsView(
            models.ConditionsModel,
            models.ConditionsModel.session,
            name='Conditions', category='Conditions'
        )
    )
    admin.add_view(
        admin_views.SymptomsView(
            models.SymptomsModel,
            models.SymptomsModel.session,
            name='Symptoms', category='Conditions'
        )
    )
    admin.add_view(
        admin_views.SuggestionView(
            models.SuggestionsModel,
            models.SuggestionsModel.session,
            name='Suggestions', category='Conditions'
        )
    )
    admin.add_view(
        admin_views.ContactView(
            models.ContactModel,
            models.ContactModel.session,
            name='Contact Info', category="Contact"
        )
    )


app.register_blueprint(kneed_help_bp)

# """ Register routes for modules """
import modules.kneed_help.routes

""" Make a folder for image resources """
os.makedirs(app.config['KNEED_HELP_IMAGES_DIR'], exist_ok=True)