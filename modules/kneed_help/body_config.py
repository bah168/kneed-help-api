import os

KNEED_HELP_IMAGES_DIR = os.path.abspath("instance/images/kneed_help")

KNEED_HELP_MODULE_ROUTES = {

    "BodyPartsList": {
        "url": "/api/body_parts",
        "methods": {
            "GET": "get all",
        }
    },
    "BodyPart": {
        "url": "/api/body_part",
        "methods": {
            "GET": "get one"
        }
    },
    "BodySubpartForBodyPart": {
        "url": "/api/sub_parts",
        "methods": {
            "GET": "get all subparts for one body part"
        }
    },
    "BodyPartImage": {
        "url": "/api/image/<string:image_name>",
        "methods": {
            "GET": "get image"
        }
    }
}


BODY_PARTS = {

    "1": {"name": "Knee", "image_name": "892d7ab4-50de-11e9-b34d-32001087a000.jpg", "active": True}
}

BODY_SUBPARTS = {

    "1": {"name": "IT Band", "coordinates": None, "active": True, "body_part_id": 1},
    "2": {"name": "Outside of Knee", "coordinates": None, "active": True, "body_part_id": 1},
    "3": {"name": "Below Knee Cap", "coordinates": None, "active": True, "body_part_id": 1},
    "4": {"name": "Inside of Knee", "coordinates": None, "active": True, "body_part_id": 1},
    "5": {"name": "Knee Cap", "coordinates": None, "active": True, "body_part_id": 1},
    "6": {"name": "Above Knee Cap", "coordinates": None, "active": True, "body_part_id": 1}
}