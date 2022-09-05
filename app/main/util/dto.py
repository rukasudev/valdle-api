""" Data Transfer Objects (DTOs) to Swagger Documentation. """

from flask_restx import Namespace, fields


class UserDto:
    api = Namespace("users", description="operações relacionadas a usuário")
    user = api.model(
        "users",
        {
            "email": fields.String(required=True, description="Email do usuário"),
            "name": fields.String(required=True, description="Nome do usuário"),
            "password": fields.String(required=True, description="Senha do usuário"),
            "public_id": fields.String(description="ID público do usuário"),
        },
    )


class AuthDto:
    api = Namespace("auth", description="operações relacionadas a autenticação")
    user_auth = api.model(
        "autenticação",
        {
            "email": fields.String(required=True, description="O endereço de email"),
            "password": fields.String(
                required=True, description="Senha de autenticação"
            ),
        },
    )


class BundleDto:
    api = Namespace("bundle", description="operações relacionadas a bundles")
    bundle = api.model(
        "random_bundle",
        {
            "bundle_image": fields.String(required=True, description="Image of bundle"),
            "answer": fields.String(
                required=True, description="Correct answer of bundle"
            ),
            "choices": fields.List(fields.String),
        },
    )
