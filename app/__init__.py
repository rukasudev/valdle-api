from flask_restx import Api
from flask import Blueprint

from .main.controller.user_controller import api as user_ns
from .main.controller.auth_controller import api as auth_ns
from .main.controller.bundle_controller import api as bundle_ns

blueprint = Blueprint(name="api", import_name=__name__, url_prefix="/api/v1")

api = Api(blueprint, title="Valdle API", version="1.0", description="", doc="/swagger")

api.add_namespace(user_ns)
api.add_namespace(auth_ns)
api.add_namespace(bundle_ns)
