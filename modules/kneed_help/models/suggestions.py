from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Table
from sqlalchemy.orm import relationship
from modules.extensions import BaseModel


class SuggestionsModel(BaseModel):
    __tablename__ = 'suggestions'

    id = Column(Integer, primary_key=True)
    name = Column('name', String(80))
    link = Column('link', String(80))
    video_start = Column(Integer)
    video_end = Column(Integer)
    description = Column('description', String(500))
    active = Column('active', Boolean, default=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
