from flask_restx import Namespace, fields


api = Namespace("auth", description="Auth operations")
user_auth = api.model(
    "authentication",
    {
        "email": fields.String(required=True, description="Auth email"),
        "password": fields.String(required=True, description="Auth password"),
    },
)
