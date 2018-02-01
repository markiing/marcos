from sqlalchemy import Column, String, Integer, PickleType
from db import db


class UserModel(db.Model):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(80))
    name = Column(String(80))
    password = Column(String(80))
    notas = PickleType()

    def __init__(self, username, password, name=None):
        self.username = username
        self.password = password
        self.name = name

    def to_json(self):
        return {
            'id': self.id,
            'username': self.username,
            'name': self.name,
            'password': self.password
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_by_id(self, id):
        result = UserModel.query.filter_by(id=id).first()
        return result

    @classmethod
    def get_by_username(self, username):
        result = UserModel.query.filter_by(username=username).first()
        return result
