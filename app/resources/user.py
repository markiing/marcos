from flask_restful import Resource, reqparse
from models.user import UserModel


class UserResource(Resource):
    def get(self, id):
        user = UserModel.get_by_id(id)
        if user:
            return user.to_json()
        else:
            return {'message': 'Username {} não encontrado'.format(id)}

    def post(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument(
            "username",
            dest="username",
            required=True
        )
        parser.add_argument(
            "password",
            dest="password",
            required=True
        )

        if UserModel.get_by_id(id):
            return {"message": "Usuario ja existe"}, 400

        args = parser.parse_args()

        if UserModel.get_by_username(args["username"]):
            return {"message": "Username já se encontra cadastrado"}, 400
        user = UserModel(**args)
        user.save()
        return {"message": "Usuario '{}' criado.".format(user.username)}, 201

    def delete(self, id):
        user = UserModel.get_by_id(id)
        if user:
            user.delete()
            return {
                "message": "Usuario '{}' deletado.".format(user.username)
            }, 200

        return {"message": "Usuario nao encontrado"}, 400

    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument(
            "password",
            dest="password",
            required=True
        )
        parser.add_argument(
            "name",
            dest="name",
            required=True
        )

        args = parser.parse_args()

        if args:
            user = UserModel.get_by_id(id)
            if user:
                user = UserModel(
                    user.username, password=args['password'], name=args['name']
                )
                user.save()
                return {'message': 'Recurso atualizado'}, 200
            else:
                return {"message": "Usuario nao encontrado"}, 400
        else:
            return {'message': 'JSON vazio'}, 204

    def patch(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument(
            "password",
            dest="password",
            required=False
        )
        parser.add_argument(
            "name",
            dest="name",
            required=False
        )

        args = parser.parse_args()
        if args:
            user = UserModel.get_by_id(id)
            if user:
                if args['password']:
                    user.password = args['password']
                if args['name']:
                    user.name = args['name']
                user.save()
                return {'message': 'Recurso atualizados'}, 200
            else:
                return {"message": "Usuario nao encontrado"}, 400
        else:
            return {'message': 'JSON vazio'}, 204
