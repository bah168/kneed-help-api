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
        symptoms = app.config.get("SYMPTOMS")
        symptoms_model = get_class_by_tablename("symptoms")

        current_records = symptoms_model.query.all()

        if current_records:
            for key, value in symptoms.items():
                if not symptoms_model.find(key):
                    symptoms_model.create(id=key,
                                            name=value['name'],
                                            active=value['active']
                                            )

        else:
            for key, value in symptoms.items():
                symptoms_model.create(id=key,
                                        name=value['name'],
                                        active=value['active']
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
        suggestions = app.config.get("SUGGESTIONS")
        suggestions_model = get_class_by_tablename("suggestions")

        current_records = suggestions_model.query.all()

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

    try:
        conditions = app.config.get("CONDITIONS")
        conditions_model = get_class_by_tablename("conditions")
        symptoms_model = get_class_by_tablename("symptoms")
        suggestions_model = get_class_by_tablename("symptoms")
        symptom_relation = app.config.get("CONDITION_SYMPTOM_RELATION")
        suggestion_relation = app.config.get("CONDITION_SUGGESTION_RELATION")

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

        for key, value in symptom_relation.items():
            condition = conditions_model.query.filter(conditions_model.id == value['condition_id']).first()
            symptom = symptoms_model.query.filter(symptoms_model.id == value['symptom_id']).first()
            condition.symptoms.append(symptom)

        # for key, value in suggestion_relation.items():
        #     condition = conditions_model.query.filter(conditions_model.id == value['condition_id']).first()
        #     suggestion = suggestions_model.query.filter(suggestions_model.id == value['suggestion_id']).first()
        #     condition.suggestions.append(suggestion)

        try:
            conditions_model.session.commit()
        except IntegrityError as err:
            print("Error seeding the database: ", err)

    except Exception as e:
        conditions_model.session.rollback()
        print(e)
        print('Condition records already exist in database.')

    try:
        body_subparts_model = get_class_by_tablename("subparts")
        relationship = app.config.get("SUBPARTS_CONDITION_RELATION")
        conditions_model = get_class_by_tablename("conditions")

        for key, value in relationship.items():
            subpart = body_subparts_model.query.filter(body_subparts_model.id == value['subpart_id']).first()
            condition = conditions_model.query.filter(conditions_model.id == value['condition_id']).first()
            subpart.conditions.append(condition)
        try:
            body_subparts_model.session.commit()
        except IntegrityError as err:
            print("Error seeding the database: ", err)

    except Exception as e:
        body_subparts_model.session.rollback()
        print(e)
        print('Subparts Relation records already exist in database.')



if __name__ == '__main__':
    seed()
