from xmlrpc.client import boolean
from flask import request
from flask_restx import Resource

from ..util.dto import AgentDTO
from ..service.agent_service import get_all_agents_with_order_by

api = AgentDTO.api
_agent = AgentDTO.agent


@api.route("", strict_slashes=False)
class AgentList(Resource):
    @api.doc("List of all agents")
    @api.marshal_list_with(_agent)
    def get(self):
        args = request.args
        language = args.get("language")
        order_by_name = args.get("order_by_name")
        is_order = order_by_name == "true"

        return get_all_agents_with_order_by(language, is_order)
