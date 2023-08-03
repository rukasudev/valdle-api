from flask_restx import Namespace, fields

api = Namespace("valdle", description="Valdle minigame operations")
valdle = api.model(
    "valdle",
    {
        "attempt": fields.String(required=True, description="word attempty"),
    },
)
