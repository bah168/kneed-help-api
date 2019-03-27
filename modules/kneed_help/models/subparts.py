# kneed_help/models/subparts.py
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Table
from sqlalchemy.orm import relationship

from modules.extensions import BaseModel


# table stores the many to many relationship between subparts and conditions
subparts_conditions_relationship = Table(
    'subparts_conditions_relationship', BaseModel.metadata,
    Column('subpart_id', Integer, ForeignKey('subparts.id')),
    Column('condition_id', Integer, ForeignKey('conditions.id'))
)


class SubpartsModel(BaseModel):
    __tablename__ = 'subparts'

    id = Column(Integer, primary_key=True)
    name = Column('name', String(80), unique=True, nullable=False)
    coordinates = Column('coordinates', String(20))
    active = Column('active', Boolean, default=True)
    body_part_id = Column(Integer, ForeignKey('body_parts.id'))
    conditions = relationship("ConditionsModel", secondary=subparts_conditions_relationship, backref="subparts")

    def __str__(self):
        return self.name


