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




if __name__ == '__main__':
    seed()
