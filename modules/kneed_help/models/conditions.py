# kneed_help/models/conditions.py
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Table
from sqlalchemy.orm import relationship
from modules.extensions import BaseModel

conditions_symptoms_relationship = Table(
    'conditions_symptoms_relationship', BaseModel.metadata,
    Column('condition_id', Integer, ForeignKey('conditions.id')),
    Column('symptom_id', Integer, ForeignKey('symptoms.id'))
)

class ConditionsModel(BaseModel):
    __tablename__ = 'conditions'

    id = Column(Integer, primary_key=True)
    name = Column('name', String(80), unique=True, nullable=False)
    active = Column('active', Boolean, default=True)
    symptoms = relationship("SymptomsModel", secondary=conditions_symptoms_relationship, backref="conditions")

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def json(self, matches):
        return_json = {
            'id': self.id,
            'name': self.name,
            'active': self.active,
            'matches': matches,
        }

        return return_json

