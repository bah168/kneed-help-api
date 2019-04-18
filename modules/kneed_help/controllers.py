from flask_restful import Resource, reqparse
from flask import jsonify, send_from_directory, current_app, abort
from .models.serializers import body_parts_schema, body_subparts_schema, body_part_schema
from .models import PartOfBodyModel, SubpartsModel


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


class BodyPartImage(Resource):

    def get(self, image_name):
        try:
            return send_from_directory(current_app.config['KNEED_HELP_IMAGES_DIR'], image_name)
        except:
            return abort('Filename not found.')


