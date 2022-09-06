""" Data Transfer Objects (DTOs) to Swagger Documentation. """

from flask_restx import Namespace, fields


class UserDto:
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


class AuthDto:
    api = Namespace("auth", description="Auth operations")
    user_auth = api.model(
        "authentication",
        {
            "email": fields.String(required=True, description="Auth email"),
            "password": fields.String(required=True, description="Auth password"),
        },
    )


class AgentDTO:
    api = Namespace("agents", description="Agent operations")
    agent = api.model(
        "agent",
        {
            "uuid": fields.String(required=True, description="Agent uuid"),
            "agent_name": fields.String(required=True, description="Agent name"),
            "description": fields.String(
                required=True, description="Agent description"
            ),
            "display_icon": fields.String(
                required=True, description="Agent display icon"
            ),
            "portrait_banner": fields.String(
                required=True, description="Agent portrait banner"
            ),
            "background_banner": fields.String(
                required=True, description="BAgent background banner"
            ),
            "agent_colors": fields.List(fields.String),
        },
    )


class BundleDto:
    api = Namespace("bundles", description="Bundle operations")
    bundle = api.model(
        "bundle",
        {
            "bundle_image": fields.String(required=True, description="Image of bundle"),
            "answer": fields.String(
                required=True, description="Correct answer of bundle"
            ),
            "choices": fields.List(fields.String),
        },
    )
