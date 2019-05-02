from sqlalchemy import Column, Integer, String

from modules.extensions import BaseModel


class ContactModel(BaseModel):
    __tablename__ = 'contact'

    id = Column(Integer, primary_key=True)
    email = Column('email', String(80), nullable=False)

