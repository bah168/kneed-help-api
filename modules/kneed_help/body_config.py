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
            "GET": "get all results"
        }
    },
    "OneResult": {
        "url": "/api/result",
        "methods": {
            "GET": "get all suggestions"
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
    "1": {"name": "Illotial Band Syndrome (ITBS)", "active": True, "description": "A painful condition in which connective tissue rubs against the thighbone."},
    "2": {"name": "Meniscus Tear", "active": True, "description": "A common injury in which forceful twisting causes certain tissue in the knee to tear."},
    "3": {"name": "Arthritis", "active": True, "description": ""},
    "4": {"name": "Osgood-Schlatter Disease", "active": True, "description": "A childhood repetitive use injury that causes a painful lump below the kneecap."},
    "5": {"name": "Jumper's Knee (Patellar Tendonitis)", "active": True, "description": "An injury to the tissue connecting the kneecap to the shin bone (patellar tendon)."},
    "6": {"name": "Patellofermoral Instability", "active": True, "description": ""},
    "7": {"name": "ACL Tear", "active": True, "description": ""},
    "8": {"name": "PCL Tear", "active": True, "description": ""},
    "9": {"name": "MCL Injury", "active": True, "description": ""},
    "10": {"name": "Osteoarthritis", "active": True, "description": "A type of arthritis that occurs when flexible tissue at the ends of bones wears down."},
    "11": {"name": "Rheumatoid Arthritis", "active": True, "description": "A chronic inflammatory disorder affecting many joints, including those in the hands and feet."},
    "12": {"name": "Pes Anserine Bursitis", "active": True, "description": ""},
    "13": {"name": "Medial Plica Irritation", "active": True, "description": ""},
    "14": {"name": "Knee Contusion", "active": True, "description": ""},
    "15": {"name": "Medial Meniscus Injury", "active": True, "description": ""},
    "16": {"name": "Runner's Knee (Chondromalacia Patellae)", "active": True, "description": ""},
    "17": {"name": "Prepatellar Bursitis", "active": True, "description": ""},
    "18": {"name": "Patellar Subluxation", "active": True, "description": ""},
    "19": {"name": "Kneecap Dislocation", "active": True, "description": ""},
    "20": {"name": "Patellar Tendon Tear", "active": True, "description": ""},
    "21": {"name": "Patellofermoral Pain Syndrome", "active": True, "description": ""},
    "22": {"name": "Quadriceps Tendonitis", "active": True, "description": ""}


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

SYMPTOMS = {

}

SUGGESTIONS = {

    "1": {"name": "Side-lying Iliotibial Band Stretch",
           "description": "Lie on your side with your affected knee on top. Bend your top knee and grab your ankle."
                          " Pull back a bit, and then place your bottom foot on the side of your top knee. "
                          "Gently pull the foot on your knee down towards the floor, elongating the outside part of "
                          "your top thigh. Hold the stretch for 15 to 20 seconds, and then release. Repeat 3 to 5 "
                          "times.", "link": "https://www.youtube.com/embed/M0e8FPL787E", "video_start": 120, "video_end": 136,
            "active": True},
    "2": {"name": "Seated Hip and ITB Stretch",
           "description": "Sit with your legs extended out in front of you. Cross the involved (hurting) leg over "
                          "your other leg, bending your knee and placing your foot flat on the floor. Rotate your body "
                          "to look over the shoulder on the involved side until you feel a stretch. Hold for 30 "
                          "seconds. Repeat four more times.", "link": "https://www.youtube.com/embed/hINHivWzmZI",
          "video_start": 0, "video_end": 23,"active": True},
    "3": {"name": "The Standing ITB Stretch",
           "description": "Stand upright. Cross the involved (hurting) leg BEHIND the opposite leg."
                          " Lean to the uninvolved side (away from the sore side) until you feel a stretch across "
                          "the affected iliotibial band. Hold for 30 seconds. Uncross your legs and stand up straight "
                          "again. Repeat four more times.", "link": "https://www.youtube.com/embed/NLkVMpkrRp0",
          "video_start": 0, "video_end": 48,"active": True},
    "4": {"name": "Knee to Opposite Shoulder Stretch",
           "description": "Lie on your back. Bend the knee of the involved (hurting) leg. Grasp behind the bent leg's "
                          "knee with both hands and pull the involved leg toward the opposite shoulder. "
                          "Hold for 30 seconds. Relax your leg. Repeat four more times.",
          "link": "https://www.youtube.com/embed/exnzCbnoENE","video_start": 0, "video_end": 60,"active": True},
    "5": {"name": "Passive Knee Extension", "description": "Do this exercise if you are unable to extend your knee"
                                                           " fully. While lying on your back, place a rolled-up towel "
                                                           "under the heel of your injured leg so the heel is about "
                                                           "6 inches off the ground. Relax your leg muscles and let "
                                                           "gravity slowly straighten your knee. Try to hold this "
                                                           "position for 2 minutes. Repeat 3 times.",
          "link": "https://www.youtube.com/embed/cshIWZiplss", "video_start": 7, "video_end": 31, "active": True},
    "6": {"name": "Heel Slide", "description": "Sit on a firm surface with your legs straight in front of you. Slowly "
                                               "slide the heel of the foot on your injured side toward your buttock by "
                                               "pulling your knee toward your chest as you slide the heel. Return to "
                                               "the starting position. Do 2 sets of 15.",
          "link": "https://www.youtube.com/embed/4_ssBADWinU", "video_start": 0, "video_end": 30, "active": True},
    "7": {"name": "Standing calf stretch", "description": "Stand facing a wall with your hands on the wall at about "
                                                          "eye level. Keep your injured leg back with your heel on the "
                                                          "floor. Keep the other leg forward with the knee bent."
                                                          " Turn your back foot slightly inward (as if you were "
                                                          "pigeon-toed). Slowly lean into the wall until you feel a "
                                                          "stretch in the back of your calf. Hold the stretch for 15 "
                                                          "to 30 seconds. Return to the starting position. Repeat 3 "
                                                          "times.",
          "link": "https://www.youtube.com/embed/ZEXriW_Bx4E", "video_start": 7, "video_end": 44, "active": True},
    "8": {"name": "Hamstring Stretch On Wall", "description": "Lie on your back with your buttocks close to a doorway. "
                                                              "Stretch your uninjured leg straight out in front of you "
                                                              "on the floor through the doorway. Raise your injured "
                                                              "leg and rest it against the wall next to the door "
                                                              "frame. Keep your leg as straight as possible. "
                                                              "You should feel a stretch in the back of your thigh. "
                                                              "Hold this position for 15 to 30 seconds. Repeat "
                                                              "3 times.",
          "link": "https://www.youtube.com/embed/2U4ChnuL3JM", "video_start": 0, "video_end": 32, "active": True},
    "9": {"name": "Quadriceps Setting", "description": "Lie on your back with the leg you want to exercise straight. "
                                                       "Place a small rolled towel underneath the knee. Slowly tighten "
                                                       "the muscle on top of the thigh (quadriceps) and push the back "
                                                       "of the knee down into the rolled towel. Hold contraction for "
                                                       "5 seconds and then slowly release, resting 5 seconds "
                                                       "between each contraction. Perform 3 sets of 10 repetitions, "
                                                       "1 time daily.",
          "link": "https://www.youtube.com/embed/THPRV2x5kaE", "video_start": 0, "video_end": 16, "active": True},
    "10": {"name": "Straight Leg Raise", "description": "Lie on your back with the leg you want to exercise straight. "
                                                        "The other knee should be bent to support your lower back. "
                                                        "Tighten the muscle on the top of your thigh and lift to the "
                                                        "level of your other knee. Slowly lower. Perform 3 sets of 10 "
                                                        "repetitions, 1 time daily.",
          "link": "https://www.youtube.com/embed/lce6GqtfHzM", "video_start": 0, "video_end": 79, "active": True},
    "11": {"name": "Hamstring Stretch", "description": "Lie on your back with the leg to be stretched straight with a "
                                                       "strap around the bottom of your foot. Using the strap for "
                                                       "support, elevate your leg until you feel a gentle stretch at "
                                                       "the back of you knee and thigh. Hold for up to 30 seconds. "
                                                       "Slowly lower. Perform 3 repetitions, 1 time daily.",
          "link": "https://www.youtube.com/embed/Dqfs4TraGjc", "video_start": 38, "video_end": 78, "active": True}

}