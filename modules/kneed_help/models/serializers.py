from modules.extensions import ma
from .body import PartOfBodyModel
from .subparts import SubpartsModel
from .symptoms import SymptomsModel
from .results import ResultsModel
from .suggestions import SuggestionsModel
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


class SymptomsSchema(ModelSchema):
    class Meta:
        model = SymptomsModel


class ConditionsSchema(ModelSchema):
    class Meta:
        model = ConditionsModel


class ResultsSchema(ModelSchema):
    class Meta:
        model = ResultsModel

class SuggestionsSchema(ModelSchema):
    class Meta:
        model = SuggestionsModel


body_parts_schema = BodyPartSchema(many=True)
body_part_schema = BodyPartSchema()
body_subparts_schema = BodySubpartSchema(many=True)
symptoms_schema = SymptomsSchema(many=True)
conditions_schema = ConditionsSchema(many=True)
condition_schema = ConditionsSchema()
results_schema = ResultsSchema(many=True)
suggestions_schema = SuggestionsSchema(many=True)

