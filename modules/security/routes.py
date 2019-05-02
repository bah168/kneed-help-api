from importlib import import_module
from modules import app

from . import security_api

with app.app_context():
    api_config = app.config.get("SECURITY_MODULE_ROUTES")
    if api_config:
        security_resources = import_module("modules.security.controllers")
        for api_name in api_config.keys():
            if api_config[api_name].get("url") is None:
                continue
            api_resource = getattr(security_resources, api_name)

            security_api.add_resource(
                api_resource, *(api_config[api_name]['url'], api_config[api_name]['url'] + '/')
            )
    else:
        print("Error: Failed to load routes for the security module.")