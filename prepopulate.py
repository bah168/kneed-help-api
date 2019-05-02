# prepopulate.py
from sqlalchemy.exc import IntegrityError

from modules import app
from modules.extensions import get_class_by_tablename

def seed():
    """
    Populates the database with config information
    """

    try:
        body_parts = app.config.get("BODY_PARTS")
        body_parts_model = get_class_by_tablename("body_parts")

        current_records = body_parts_model.query.all()

        if current_records:
            for key, value in body_parts.items():
                    if not body_parts_model.find(key):

                        body_parts_model.create(id=key, name=value)

        else:

            for key, value in body_parts.items():
                body_parts_model.create(id=key, name=value)

        try:
            body_parts_model.session.commit()
        except IntegrityError as err:
            print("Error seeding the database: ", err)

    except:
        body_parts_model.session.rollback()
        print('Body parts records already exist in database.')

    try:
        body_subparts = app.config.get("BODY_SUBPARTS")
        body_subparts_model = get_class_by_tablename("subparts")

        current_records = body_subparts_model.query.all()

        if current_records:
            for key, value in body_subparts.items():
                    if not body_subparts_model.find(key):
                        body_subparts_model.create(id=key,
                                                   name=value['name'],
                                                   coordinates=value['coordinates'],
                                                   active=value['active'],
                                                   body_part_id=value['body_part_id']
                                                   )

        else:
            for key, value in body_subparts.items():

                body_subparts_model.create(id=key,
                                           name=value['name'],
                                           coordinates=value['coordinates'],
                                           active=value['active'],
                                           body_part_id=value['body_part_id']
                                           )
        try:
            body_subparts_model.session.commit()
        except IntegrityError as err:
            print("Error seeding the database: ", err)

    except Exception as e:
        body_subparts_model.session.rollback()
        print(e)
        print('Subparts records already exist in database.')

    try:
        conditions = app.config.get("CONDITIONS")
        conditions_model = get_class_by_tablename("conditions")

        current_records = conditions_model.query.all()

        if current_records:
            for key, value in conditions.items():
                if not conditions_model.find(key):
                    conditions_model.create(id=key,
                                            name=value['name'],
                                            active=value['active'],
                                            description=value['description']
                                            )

        else:
            for key, value in conditions.items():
                conditions_model.create(id=key,
                                        name=value['name'],
                                        active=value['active'],
                                        description=value['description']
                                        )
        try:
            conditions_model.session.commit()
        except IntegrityError as err:
            print("Error seeding the database: ", err)

    except Exception as e:
        conditions_model.session.rollback()
        print(e)
        print('Condition records already exist in database.')


    try:
        symptoms = app.config.get("SYMPTOMS")
        symptoms_model = get_class_by_tablename("symptoms")

        current_records = symptoms_model.query.all()

        if current_records:
            for key, value in symptoms.items():
                if not symptoms_model.find(key):
                    symptoms_model.create(id=key,
                                            name=value['name'],
                                            active=value['active'],
                                            description=value['description']
                                            )

        else:
            for key, value in symptoms.items():
                symptoms_model.create(id=key,
                                        name=value['name'],
                                        active=value['active'],
                                        description=value['description']
                                        )
        try:
            symptoms_model.session.commit()
        except IntegrityError as err:
            print("Error seeding the database: ", err)

    except Exception as e:
        symptoms_model.session.rollback()
        print(e)
        print('Symptom records already exist in database.')


    try:
        suggestions = app.config.get("SYMPTOMS")
        suggestions_model = get_class_by_tablename("symptoms")

        current_records = symptoms_model.query.all()

        if current_records:
            for key, value in suggestions.items():
                if not suggestions_model.find(key):
                    suggestions_model.create(id=key,
                                             name=value['name'],
                                             active=value['active'],
                                             description=value['description'],
                                             link=value['link'],
                                             video_start=value['video_start'],
                                             video_end=value['video_end']
                                            )

        else:
            for key, value in suggestions.items():
                suggestions_model.create(id=key,
                                         name=value['name'],
                                         active=value['active'],
                                         description=value['description'],
                                         link=value['link'],
                                         video_start=value['video_start'],
                                         video_end=value['video_end']
                                         )
        try:
            suggestions_model.session.commit()
        except IntegrityError as err:
            print("Error seeding the database: ", err)

    except Exception as e:
        suggestions_model.session.rollback()
        print(e)
        print('Suggestion records already exist in database.')

    # try:
    #     subpart_condition_relation = app.config.get("SUBPARTS_CONDITION_RELATION")
    #     subpart_condition_relation_model = get_class_by_tablename("subparts_conditions_relationship")
    #
    #     current_records = subpart_condition_relation_model.query.all()
    #
    #     if current_records:
    #         for key, value in subpart_condition_relation.items():
    #             if not subpart_condition_relation_model.find(key):
    #                 subpart_condition_relation_model.create(id=key,
    #                                                         subpart_id=value['subpart_id'],
    #                                                         condition_id=value['condition_id']
    #                                                         )
    #
    #     else:
    #         for key, value in subpart_condition_relation.items():
    #             subpart_condition_relation_model.create(id=key,
    #                                                     subpart_id=value['subpart_id'],
    #                                                     condition_id=value['condition_id']
    #                                                     )
    #     try:
    #         subpart_condition_relation_model.session.commit()
    #     except IntegrityError as err:
    #         print("Error seeding the database: ", err)
    #
    # except Exception as e:
    #     subpart_condition_relation_model.session.rollback()
    #     print(e)
    #     print('Subpart and condition relation records already exist in database.')




if __name__ == '__main__':
    seed()
