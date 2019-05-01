from modules.extensions import ma
from .body import PartOfBodyModel
from .subparts import SubpartsModel
from .conditions import ConditionsModel
from marshmallow_sqlalchemy import ModelSchema


class BodyPartSchema(ModelSchema):
    class Meta:
        model = PartOfBodyModel

class BodySubpartSchema(ModelSchema):
    class Meta:
        model = SubpartsModel
        
class ConditionsSchema(ModelSchema): 
    class Meta:
        model = ConditionsModel


body_parts_schema = BodyPartSchema(many=True)
body_subparts_schema = BodySubpartSchema(many=True)
condition_schema = ConditionsModel()
