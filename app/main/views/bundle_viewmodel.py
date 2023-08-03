from flask_restx import Namespace, fields

api = Namespace("bundles", description="Bundle operations")
bundle = api.model(
    "bundle",
    {
        "bundle_image": fields.String(required=True, description="Image of bundle"),
        "answer": fields.String(required=True, description="Correct answer of bundle"),
        "choices": fields.List(fields.String),
    },
)
