import jwt
import random
from flask import current_app, jsonify, abort
from flask_restful import Resource, reqparse
from datetime import datetime, timedelta


class Authorize(Resource):

    def get(self):

        user_id = random.randint(1, 1000000000)

        payload = {
            'identity': user_id,
            'iat': datetime.utcnow(),
            'exp': datetime.utcnow() + timedelta(minutes=30),
            'nbf': datetime.utcnow(),
        }

        token = jwt.encode(payload, current_app.config['SECRET_KEY'])

        return jsonify(
            access_token=token.decode('UTF - 8')

        )


class RefreshToken(Resource):

    def __init__(self):
        parser = reqparse.RequestParser()
        parser.add_argument("Authorization", location="headers")
        self.args = parser.parse_args()
        super().__init__()

    def get(self):
        auth_header = self.args['Authorization']
        if auth_header:
            token = self.args['Authorization'].split(" ")[1]
        else:
            token = ''

        try:
            payload = jwt.decode(token, current_app.config['SECRET_KEY'])
        except jwt.InvalidTokenError as err:
            return abort(401, err)
        else:
            new_payload = {
                'identity': payload['identity'],
                'iat': datetime.utcnow(),
                'exp': datetime.utcnow() + timedelta(minutes=30),
                'nbf': datetime.utcnow(),
            }


            token = jwt.encode(new_payload, current_app.config['SECRET_KEY'])
            return jsonify(
                access_token=token.decode('UTF - 8')
            )

