from flask import Flask
from flask_restful import Api

from resources.user import UserResource
from resources.ping import Ping


app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')

api = Api(app)


api.add_resource(UserResource, '/user/<int:id>')
api.add_resource(Ping, '/ping')


if __name__ == "__main__":
    from db import db
    db.init_app(app)

    if app.config['DEBUG']:
        @app.before_first_request
        def create_tables():
            db.drop_all()
            db.create_all()

    app.run()
