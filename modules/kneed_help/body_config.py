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
    },
    "ContactUs": {
        "url": "/api/contact_us",
        "methods": {
            "POST": "posting email"
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
    "3": {"name": "Osgood-Schlatter Disease", "active": True, "description": "A childhood repetitive use injury that causes a painful lump below the kneecap."},
    "4": {"name": "Jumper's Knee (Patellar Tendonitis)", "active": True, "description": "An injury to the tissue connecting the kneecap to the shin bone (patellar tendon)."},
    "5": {"name": "Patellofermoral Pain Syndrome", "active": True, "description": "A condition in which the cartilage under the kneecap is damaged due to injury or overuse."},
    "6": {"name": "ACL Injury", "active": True, "description": ""},
    "7": {"name": "PCL Injury", "active": True, "description": ""},
    "8": {"name": "MCL Injury", "active": True, "description": ""},
    "9": {"name": "Osteoarthritis", "active": True, "description": "A type of arthritis that occurs when flexible tissue at the ends of bones wears down."},
    "10": {"name": "Rheumatoid Arthritis", "active": True, "description": "A chronic inflammatory disorder affecting many joints, including those in the hands and feet."},
    "11": {"name": "Pes Anserine Bursitis", "active": True, "description": ""},
    "12": {"name": "Medial Plica Irritation", "active": True, "description": ""},
    "13": {"name": "Knee Contusion", "active": True, "description": ""},
    "14": {"name": "Medial Meniscus Injury", "active": True, "description": ""},
    "15": {"name": "Runner's Knee (Chondromalacia Patellae)", "active": True, "description": ""},
    "16": {"name": "Prepatellar Bursitis", "active": True, "description": ""},
    "17": {"name": "Patellar Subluxation", "active": True, "description": ""},
    "18": {"name": "Kneecap Dislocation", "active": True, "description": ""},
    "19": {"name": "Patellar Tendon Tear", "active": True, "description": ""},
    "20": {"name": "Quadriceps Tendonitis", "active": True, "description": ""}


}


SUBPARTS_CONDITION_RELATION = {
    "1": {"subpart_id": 1, "condition_id": 1},
    "2": {"subpart_id": 2, "condition_id": 2},
    "3": {"subpart_id": 2, "condition_id": 9},
    "4": {"subpart_id": 2, "condition_id": 10},
    "5": {"subpart_id": 2, "condition_id": 1},
    "6": {"subpart_id": 3, "condition_id": 3},
    "7": {"subpart_id": 3, "condition_id": 4},
    "8": {"subpart_id": 3, "condition_id": 5},
    "9": {"subpart_id": 4, "condition_id": 6},
    "10": {"subpart_id": 4, "condition_id": 7},
    "11": {"subpart_id": 4, "condition_id": 8},
    "12": {"subpart_id": 4, "condition_id": 9},
    "13": {"subpart_id": 4, "condition_id": 10},
    "14": {"subpart_id": 4, "condition_id": 11},
    "15": {"subpart_id": 4, "condition_id": 12},
    "16": {"subpart_id": 4, "condition_id": 13},
    "17": {"subpart_id": 4, "condition_id": 14},
    "18": {"subpart_id": 5, "condition_id": 15},
    "19": {"subpart_id": 5, "condition_id": 16},
    "20": {"subpart_id": 5, "condition_id": 17},
    "21": {"subpart_id": 5, "condition_id": 18},
    "22": {"subpart_id": 5, "condition_id": 19},
    "23": {"subpart_id": 5, "condition_id": 5},
    "24": {"subpart_id": 6, "condition_id": 20},

}


CONDITION_SYMPTOM_RELATION = {
    "1": {"condition_id": 1, "symptom_id": 1},
    "2": {"condition_id": 1, "symptom_id": 6},
    "3": {"condition_id": 2, "symptom_id": 1},
    "4": {"condition_id": 2, "symptom_id": 2},
    "5": {"condition_id": 2, "symptom_id": 3},
    "6": {"condition_id": 2, "symptom_id": 4},
    "7": {"condition_id": 2, "symptom_id": 5},
    "8": {"condition_id": 9, "symptom_id": 1},
    "9": {"condition_id": 9, "symptom_id": 4},
    "10": {"condition_id": 9, "symptom_id": 5},
    "11": {"condition_id": 9, "symptom_id": 6},
    "12": {"condition_id": 9, "symptom_id": 7},
    "13": {"condition_id": 9, "symptom_id": 8},
    "14": {"condition_id": 9, "symptom_id": 9},
    "15": {"condition_id": 9, "symptom_id": 10},
    "16": {"condition_id": 10, "symptom_id": 1},
    "17": {"condition_id": 10, "symptom_id": 5},
    "18": {"condition_id": 10, "symptom_id": 8},
    "19": {"condition_id": 10, "symptom_id": 10},
    "20": {"condition_id": 10, "symptom_id": 11},
    "21": {"condition_id": 10, "symptom_id": 12},
    "22": {"condition_id": 3, "symptom_id": 14},
    "23": {"condition_id": 3, "symptom_id": 15},
    "25": {"condition_id": 4, "symptom_id": 5},
    "26": {"condition_id": 4, "symptom_id": 15},
    "27": {"condition_id": 4, "symptom_id": 10},
    "28": {"condition_id": 4, "symptom_id": 3},
    "29": {"condition_id": 5, "symptom_id": 12},
    "30": {"condition_id": 5, "symptom_id": 5},
    "31": {"condition_id": 5, "symptom_id": 16},
    "32": {"condition_id": 5, "symptom_id": 17},

}

CONDITION_SUGGESTION_RELATION = {
    "1": {"condition_id": 1, "suggestion_id": 1},
    "2": {"condition_id": 1, "suggestion_id": 2},
    "3": {"condition_id": 1, "suggestion_id": 3},
    "4": {"condition_id": 1, "suggestion_id": 4},
    "5": {"condition_id": 2, "suggestion_id": 5},
    "6": {"condition_id": 2, "suggestion_id": 6},
    "7": {"condition_id": 2, "suggestion_id": 7},
    "8": {"condition_id": 2, "suggestion_id": 8},
    "9": {"condition_id": 9, "suggestion_id": 9},
    "10": {"condition_id": 9, "suggestion_id": 10},
    "11": {"condition_id": 9, "suggestion_id": 11},
    "12": {"condition_id": 9, "suggestion_id": 7},
    "13": {"condition_id": 10, "suggestion_id": 7},
    "14": {"condition_id": 10, "suggestion_id": 11},
    "15": {"condition_id": 10, "suggestion_id": 10},
    "16": {"condition_id": 10, "suggestion_id": 9},
    "17": {"condition_id": 3, "suggestion_id": 8},
    "18": {"condition_id": 3, "suggestion_id": 7},
    "19": {"condition_id": 3, "suggestion_id": 12},
    "20": {"condition_id": 3, "suggestion_id": 13},
    "21": {"condition_id": 4, "suggestion_id": 14},
    "22": {"condition_id": 4, "suggestion_id": 12},
    "23": {"condition_id": 4, "suggestion_id": 15},
    "24": {"condition_id": 4, "suggestion_id": 13},
    "25": {"condition_id": 5, "suggestion_id": 14},
    "26": {"condition_id": 5, "suggestion_id": 12},
    "27": {"condition_id": 5, "suggestion_id": 15},
    "28": {"condition_id": 5, "suggestion_id": 9},




}

SYMPTOMS = {

    "1": {"name": "Swelling", "active": True},
    "2": {"name": "Difficulty Extending Knee", "active": True},
    "3": {"name": "Difficulty Walking", "active": True},
    "4": {"name": "Limited Range of Motion", "active": True},
    "5": {"name": "Stiffness", "active": True},
    "6": {"name": "Pain Increases When Active", "active": True},
    "7": {"name": "Pain Decreases When Resting", "active": True},
    "8": {"name": "Feeling Warmth of Joint", "active": True},
    "9": {"name": "Crackly Sound When Moving Knee", "active": True},
    "10": {"name": "Tenderness", "active": True},
    "11": {"name": "Fatigue", "active": True},
    "12": {"name": "Weakness", "active": True},
    "13": {"name": "Pain Sensation of Pins and Needles", "active": True},
    "14": {"name": "Limping", "active": True},
    "15": {"name": "Lump", "active": True},
    "16": {"name": "Pain Increases When Climbing Stairs", "active": True},
    "17": {"name": "Pain Increases With Squatting Movements.", "active": True}




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
          "link": "https://www.youtube.com/embed/Dqfs4TraGjc", "video_start": 38, "video_end": 78, "active": True},
    "12": {"name": "Quadricep Stretch", "description": "Stand at an arm's length away from the wall with your injured "
                                                       "side farthest from the wall. Facing straight ahead, brace "
                                                       "yourself by keeping one hand against the wall. With your other "
                                                       "hand, grasp the ankle on your injured side and pull your heel "
                                                       "toward your buttocks. Don't arch or twist your back. Keep your "
                                                       "knees together. Hold this stretch for 15 to 30 seconds.",
           "link": "https://www.youtube.com/embed/CZBKSOtyssM", "video_start": 0, "video_end": 55, "active": True},
    "13": {"name": "Rectus Femoris Stretch", "description": "Kneel on your injured knee on a padded surface. Place "
                                                            "your other leg in front of you with your foot flat on the "
                                                            "floor. Keep your head and chest facing forward and upright"
                                                            " and grab the ankle behind you. Gently bring your ankle "
                                                            "back toward your buttocks until you feel a stretch in the "
                                                            "front of your thigh. Hold 15 to 30 seconds. Repeat 2 to 3 "
                                                            "times.",
           "link": "https://www.youtube.com/embed/BhQimqvU1tM", "video_start": 108, "video_end": 162, "active": True},
    "14": {"name": "Standing Hamstring Stretch", "description": "Put the heel of the leg on your injured side on a "
                                                                "stool about 15 inches high. Keep your leg straight. "
                                                                "Lean forward, bending at the hips, until you feel a "
                                                                "mild stretch in the back of your thigh. Make sure you "
                                                                "don't roll your shoulders or bend at the waist when "
                                                                "doing this or you will stretch your lower back instead "
                                                                "of your leg. Hold the stretch for 15 to 30 seconds. "
                                                                "Repeat 3 times.",
           "link": "https://www.youtube.com/embed/6vxpOglpLfY", "video_start": 19, "video_end": 77, "active": True},
    "15": {"name": "Side-lying Leg Lift", "description": "Lie on your uninjured side. Tighten the front thigh muscles "
                                                         "on your injured leg and lift that leg 8 to 10 inches "
                                                         "(20 to 25 centimeters) away from the other leg. "
                                                         "Keep the leg straight and lower it slowly. Do 2 sets of 15.",
           "link": "https://www.youtube.com/embed/Dha6wZbFLbY", "video_start": 0, "video_end": 71, "active": True},





}