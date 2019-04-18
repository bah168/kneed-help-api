from modules.extensions import ma
from .body import PartOfBodyModel
from .subparts import SubpartsModel
from marshmallow_sqlalchemy import ModelSchema


class BodyPartSchema(ModelSchema):
    class Meta:
        model = PartOfBodyModel

class BodySubpartSchema(ModelSchema):
    class Meta:
        model = SubpartsModel


body_parts_schema = BodyPartSchema(many=True)
body_part_schema = BodyPartSchema()
body_subparts_schema = BodySubpartSchema(many=True)