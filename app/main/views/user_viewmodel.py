from flask_restx import Namespace, fields

api = Namespace("users", description="User operations")
user = api.model(
    "users",
    {
        "uuid": fields.String(description="User UUUID"),
        "email": fields.String(required=True, description="User Email"),
        "name": fields.String(required=True, description="User Name"),
        "password": fields.String(required=True, description="User password"),
    },
)
