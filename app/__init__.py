from flask_restx import Api
from flask import Blueprint

from .main.controller.user_controller import api as user_ns
from .main.controller.auth_controller import api as auth_ns

blueprint = Blueprint("api", __name__)

api = Api(
    blueprint, prefix="/api/v1", title="Valdle API", version="1.0", description=""
)

api.add_namespace(user_ns)
api.add_namespace(auth_ns)
