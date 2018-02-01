from sqlalchemy import Column, String, Integer
from app import db


class UserModel(db.Model):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String)
    name = Column(String)
    password = Column(String)

    def __init__(self):
        self.username = username
        self.password = password
        self.name = name

    def to_json(self):
        return {
            'id': id,
            'username': self.username,
            'name': self.name,
            'password': self.password
        }

    @classmethod
    def get_by_id(self, id):
        result = UserModel.query.f
