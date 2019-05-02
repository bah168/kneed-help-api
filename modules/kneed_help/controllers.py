from flask_restful import Resource, reqparse
from flask import jsonify, send_from_directory, current_app, abort
from .models.serializers import body_parts_schema, body_subparts_schema, body_part_schema, symptoms_schema, \
    results_schema, condition_schema, suggestions_schema
from .models import PartOfBodyModel, SubpartsModel, SymptomsModel, ConditionsModel, ResultsModel, ContactModel
from sqlalchemy_pagination import paginate
from sqlalchemy.exc import DatabaseError
from flask_mail import Message
from modules.extensions import mail


class BodyPartsList(Resource):

    def get(self):
        body_parts = PartOfBodyModel.query.all()
        return jsonify(body_parts=body_parts_schema.dump(body_parts).data)


class BodyPart(Resource):

    def __init__(self):
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument("id", type=int)
        self.args = parser.parse_args()
        super().__init__()

    def get(self):
        body_part = PartOfBodyModel.query.filter(PartOfBodyModel.id == self.args['id']).first()
        return jsonify(body_part=body_part_schema.dump(body_part).data)


class BodySubpartForBodyPart(Resource):

    def __init__(self):
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument("id", type=int)
        self.args = parser.parse_args()
        super().__init__()

    def get(self):
        body_part_id = self.args['id']

        subparts = SubpartsModel.query.filter(SubpartsModel.body_part_id == body_part_id).all()
        return jsonify(subparts=body_subparts_schema.dump(subparts).data)


class SymptomsList(Resource):

    def __init__(self):
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument("subpart_id", type=int)
        self.args = parser.parse_args()
        super().__init__()

    def get(self):

        symptoms = []
        subpart = SubpartsModel.query.filter(SubpartsModel.id == self.args['subpart_id']).first()
        for condition in subpart.conditions:
            for symptom in condition.symptoms:
                symptoms.append(symptom)
        symptoms = list(dict.fromkeys(symptoms))

        return jsonify(symptoms=symptoms_schema.dump(symptoms).data)


class SymptomsListPagination(Resource):

    def __init__(self):
        parser = reqparse.RequestParser()
        parser.add_argument('page', type=int)
        parser.add_argument('per_page', type=int)
        parser.add_argument("subpart_id", type=int)
        self.args = parser.parse_args()
        super().__init__()

    def get(self):
        symptoms = []
        subpart = SubpartsModel.query.filter(SubpartsModel.id == self.args['subpart_id']).first()
        for condition in subpart.conditions:
            for symptom in condition.symptoms:
                symptoms.append(symptom.id)
        symptoms = list(dict.fromkeys(symptoms))

        symptoms = SymptomsModel.query.filter(SymptomsModel.id.in_(symptoms))
        query_list = paginate(symptoms, self.args['page'], self.args['per_page'])

        return jsonify(symptoms=symptoms_schema.dump(query_list.items).data)


class ResultList(Resource):

    def __init__(self):
        parser = reqparse.RequestParser()
        parser.add_argument('page', type=int)
        parser.add_argument('per_page', type=int)
        parser.add_argument("symptom_ids", type=str, action='append')
        parser.add_argument("subpart_id", type=str)
        parser.add_argument("user_id", type=int)
        self.args = parser.parse_args()
        super().__init__()

    def post(self):

        results = ResultsModel.query.all()

        if results:
            ResultsModel.query.delete()
            try:
                ResultsModel.session.commit()
            except DatabaseError:
                return abort(500, 'An error occurred while adding this record.')


        subpart = SubpartsModel.query.filter(SubpartsModel.id == self.args['subpart_id']).first()

        for condition in subpart.conditions:
            all_symptoms = []
            for symptom in condition.symptoms:
                all_symptoms.append(str(symptom.id))

            matches = set(all_symptoms).intersection(self.args['symptom_ids'])

            if len(matches) > 0:

                ResultsModel.create(
                    user_id=self.args["user_id"],
                    condition_id=condition.id,
                    condition_name=condition.name,
                    condition_description=condition.description,
                    matches=len(matches)
                 )

                try:
                    ResultsModel.session.commit()
                except DatabaseError:
                    return abort(500, 'An error occurred while adding this record.')

        return {'message': 'Results processed.'}, 201

    def get(self):
        results = ResultsModel.query.filter(ResultsModel.user_id == self.args['user_id']).order_by(ResultsModel.matches.desc())
        results_count = results.count()
        results = paginate(results, self.args['page'], self.args['per_page'])

        return jsonify(results=results_schema.dump(results.items).data,
                       count=results_count)


class OneResult(Resource):

    def __init__(self):
        parser = reqparse.RequestParser()
        parser.add_argument('condition_id', type=int)
        self.args = parser.parse_args()
        super().__init__()

    def get(self):

        condition = ConditionsModel.query.filter(ConditionsModel.id == self.args['condition_id']).first()

        suggestions = condition.suggestions

        symptoms = condition.symptoms

        return jsonify(condition=condition_schema.dump(condition).data,
                       suggestions=suggestions_schema.dump(suggestions).data,
                       symptoms=symptoms_schema.dump(symptoms).data)


class ContactUs(Resource):

    def __init__(self):
        parser = reqparse.RequestParser()
        parser.add_argument('email', type=str)
        parser.add_argument('message', type=str)
        parser.add_argument('name', type=str)
        self.args = parser.parse_args()
        super().__init__()

    def post(self):

        message = "<div>Name: " + self.args['name'] + "</div>" + "<div>Email: " + \
                  self.args['email'] + "</div>" + "<div>" + self.args['message'] + "</div>"


        msg = Message("Kneed Help Contact us",
                      recipients=['kneedhelpapp@gmail.com'])

        msg.html = message

        try:
            mail.send(msg)
        except:
            return abort(500, "An error occurred while sending email.")

        return {'message': 'Email has been sent.'}


class BodyPartImage(Resource):

    def get(self, image_name):
        try:
            return send_from_directory(current_app.config['KNEED_HELP_IMAGES_DIR'], image_name)
        except:
            return abort('Filename not found.')




