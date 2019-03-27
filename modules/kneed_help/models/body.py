# kneed_help/models/body.py
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship

from modules.extensions import BaseModel


class PartOfBodyModel(BaseModel):
    __tablename__ = 'body_parts'

    id = Column(Integer, primary_key=True)
    name = Column('name', String(20), unique=True, nullable=False)
    image_name = Column('image_name', String(80), unique=True)
    active = Column('active', Boolean, default=True)
    subparts = relationship("SubpartsModel", backref="body_parts")

    def __str__(self):
        return self.name






