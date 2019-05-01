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
    },
    "SymptomsList": {
        "url": "/api/symptoms",
        "methods": {
            "GET": "get all"
        }
    },
    "SymptomsListPagination": {
        "url": "/api/symptoms/pagination",
        "methods": {
            "GET": "get all symptoms paginated"
        }
    },

    "ResultList": {
        "url": "/api/results",
        "methods": {
            "GET": "get all rresults"
        }
    }
}


BODY_PARTS = {

    "1": {"name": "Knee", "image_name": "71b0ba9a-5ff7-11e9-ba85-8438354a7466.jpg", "active": True}
}

BODY_SUBPARTS = {

    "1": {"name": "IT Band", "coordinates": "118,4,209,235", "active": True, "body_part_id": 1},
    "2": {"name": "Outside of Knee", "coordinates": "119,236,230,423", "active": True, "body_part_id": 1},
    "3": {"name": "Below Knee Cap", "coordinates": "227,388,384,492", "active": True, "body_part_id": 1},
    "4": {"name": "Inside of Knee", "coordinates": "385,480,457,187", "active": True, "body_part_id": 1},
    "5": {"name": "Knee Cap", "coordinates": "235,231,383,387", "active": True, "body_part_id": 1},
    "6": {"name": "Above Knee Cap", "coordinates": "385,111,232,231", "active": True, "body_part_id": 1}
}

CONDITIONS = {
    "1": {"name": "Illotial Band Syndrome (ITBS)", "active": True},
    "2": {"name": "Meniscus Tear", "active": True},
    "3": {"name": "Arthritis", "active": True},
    "4": {"name": "Osgood-Schlatter Disease", "active": True},
    "5": {"name": "Jumper's Knee (Patellar Tendonitis)", "active": True},
    "6": {"name": "Patellofermoral Instability", "active": True},
    "7": {"name": "ACL Tear", "active": True},
    "8": {"name": "PCL Tear", "active": True},
    "9": {"name": "MCL Injury", "active": True},
    "10": {"name": "Osteoarthritis", "active": True},
    "11": {"name": "Rheumatoid Arthritis", "active": True},
    "12": {"name": "Pes Anserine Bursitis", "active": True},
    "13": {"name": "Medial Plica Irritation", "active": True},
    "14": {"name": "Knee Contusion", "active": True},
    "15": {"name": "Medial Meniscus Injury", "active": True},
    "16": {"name": "Runner's Knee (Chondromalacia Patellae)", "active": True},
    "17": {"name": "Prepatellar Bursitis", "active": True},
    "18": {"name": "Patellar Subluxation", "active": True},
    "19": {"name": "Kneecap Dislocation", "active": True},
    "20": {"name": "Patellar Tendon Tear", "active": True},
    "21": {"name": "Patellofermoral Pain Syndrome", "active": True},
    "22": {"name": "Quadriceps Tendonitis", "active": True}


}

SUBPARTS_CONDITION_RELATION = {
    "1": {"subpart_id": 1, "condition_id": 1},
    "2": {"subpart_id": 2, "condition_id": 1},
    "3": {"subpart_id": 2, "condition_id": 2},
    "4": {"subpart_id": 2, "condition_id": 3},
    "5": {"subpart_id": 3, "condition_id": 4},
    "6": {"subpart_id": 3, "condition_id": 5},
    "7": {"subpart_id": 3, "condition_id": 6},
    "8": {"subpart_id": 4, "condition_id": 7},
    "9": {"subpart_id": 4, "condition_id": 8},
    "10": {"subpart_id": 4, "condition_id": 9},
    "11": {"subpart_id": 4, "condition_id": 10},
    "12": {"subpart_id": 4, "condition_id": 11},
    "13": {"subpart_id": 4, "condition_id": 12},
    "14": {"subpart_id": 4, "condition_id": 13},
    "15": {"subpart_id": 4, "condition_id": 14},
    "16": {"subpart_id": 4, "condition_id": 15},
    "17": {"subpart_id": 5, "condition_id": 16},
    "18": {"subpart_id": 5, "condition_id": 17},
    "19": {"subpart_id": 5, "condition_id": 18},
    "20": {"subpart_id": 5, "condition_id": 19},
    "21": {"subpart_id": 5, "condition_id": 20},
    "22": {"subpart_id": 5, "condition_id": 21},
    "23": {"subpart_id": 6, "condition_id": 22}

}