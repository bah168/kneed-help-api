# security/models/users.py
from flask_security import UserMixin
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy import Column, Integer, String, Boolean

from modules.extensions import BaseModel

# user table model
class User(BaseModel, UserMixin):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(120), unique=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    username = Column(String(80), unique=True, nullable=False)
    password = Column(String(255), nullable=False, default='default_password')
    active = Column(Boolean, default=False)

    @hybrid_property
    def name(self):
        return "{last_name}, {first_name}".format(
            first_name=self.first_name,
            last_name=self.last_name
        )

    # set to appease flask-security
    @hybrid_property
    def roles(self):
        return []

    # set to appease flask-security
    @roles.setter
    def roles(self, role):
        pass

    # returns username
    def __repr__(self):
        return self.username
