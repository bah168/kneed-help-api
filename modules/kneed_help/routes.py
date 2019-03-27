# kneed_help/routes.py

from importlib import import_module
from modules import app

from . import kneed_help_api


with app.app_context():
    api_config = app.config.get("KNEED_HELP_MODULE_ROUTES")
    if api_config:
        kneed_help_resources = import_module("modules.kneed_help.controllers")
        for api_name in api_config.keys():
            if api_config[api_name].get("url") is None:
                continue
            api_resource = getattr(kneed_help_resources, api_name)
            kneed_help_api.add_resource(
                api_resource, *(api_config[api_name]['url'], api_config[api_name]['url'] + '/')
            )
    else:
        print("Error: Failed to load routes for the kneed help module.")
