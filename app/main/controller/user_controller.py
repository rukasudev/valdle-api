from flask import request
from flask_restx import Resource

from app.main.util.decorator import admin_token_required
from ..util.dto import UserDto
from ..service.user_service import save_new_user, get_all_users, get_a_user
from typing import Dict, Tuple

api = UserDto.api
_user = UserDto.user


@api.route("", strict_slashes=False)
class UserList(Resource):
    @api.doc("lista todos os usuários cadastrados")
    @admin_token_required
    @api.marshal_list_with(_user, envelope="data")
    def get(self):
        """Lista todos os usuários cadastrados"""
        return get_all_users()

    @api.expect(_user, validate=True)
    @api.response(201, "Successfully registered.")
    @api.response(401, "Some error occurred. Please try again.")
    @api.response(409, "User already exists. Please Log in.")
    @api.doc("cadastra um novo usuário")
    def post(self) -> Tuple[Dict[str, str], int]:
        """Cadastra um novo usuário"""
        data = request.json
        return save_new_user(data=data)


@api.route("/<public_id>")
@api.param("public_id", "ID público do usuário")
@api.response(404, "User not found.")
class User(Resource):
    @api.doc("retorna o usuário pelo seu ID público")
    @admin_token_required
    @api.marshal_with(_user)
    def get(self, public_id):
        """Retorna o usuário pelo seu ID público"""
        user = get_a_user(public_id)
        if not user:
            api.abort(404)
        else:
            return user
