from flask import Flask
from flask_restful import Api
from sqlalchemy import SQLAlchemy

from resources.user import UserResource
from resources.ping import Ping

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')

api = Api(app)

db = SQLAlchemy(app)

api.add_resource(UserResource, '/user/<int:id>')
api.add_resource(Ping, '/ping')


def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


if __name__ == "__main__":
    if app['config'] == "DEBUG":
        recreate_db()
    app.run()
