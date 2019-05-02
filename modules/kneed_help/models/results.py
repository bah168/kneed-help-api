
from sqlalchemy import Column, Integer, String
from modules.extensions import BaseModel


class ResultsModel(BaseModel):
    __tablename__ = 'results'

    id = Column(Integer, primary_key=True)
    user_id = Column('user_id', Integer, nullable=False)
    condition_id = Column('condition_id', Integer)
    condition_name = Column('condition_name', String(80), default=True)
    condition_description = Column('condition_desc', String(120))
    matches = Column('matches', Integer, default=True)

    def __str__(self):
        return self.condition_name
