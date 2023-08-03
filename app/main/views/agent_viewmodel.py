from flask_restx import Namespace, fields

api = Namespace("agents", description="Agent operations")
agent = api.model(
    "agent",
    {
        "uuid": fields.String(required=True, description="Agent uuid"),
        "agent_name": fields.String(required=True, description="Agent name"),
        "description": fields.String(required=True, description="Agent description"),
        "display_icon": fields.String(required=True, description="Agent display icon"),
        "portrait_banner": fields.String(
            required=True, description="Agent portrait banner"
        ),
        "background_banner": fields.String(
            required=True, description="Agent background banner"
        ),
        "agent_colors": fields.List(fields.String),
    },
)
ability = api.model(
    "ability",
    {
        "agent_name": fields.String(required=True, description="Agent name"),
        "agent_picture": fields.String(required=True, description="Agent picture"),
        "ability_name": fields.String(required=True, description="Ability name"),
        "ability_picture": fields.String(required=True, description="Ability picture"),
    },
)
