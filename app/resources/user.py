from flask_restful import Resource, reqparse


class UserResource(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument(
            "username",
            dest="username",
            required=True
        )
        args = parser.parse_args()

    def post(self):
        pass

    def delete(self):
        pass

    def put(self):
        pass

    def patch(self):
        pass
