# kneed_help/models/conditions.py
from sqlalchemy import Column, Integer, String, Boolean

from modules.extensions import BaseModel


class SymptomsModel(BaseModel):
    __tablename__ = 'symptoms'

    id = Column(Integer, primary_key=True)
    name = Column('name', String(80), unique=True, nullable=False)
    active = Column('active', Boolean, default=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
