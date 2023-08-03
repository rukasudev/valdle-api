from xmlrpc.client import boolean
from flask import request
from flask_restx import Resource

from ..views import agent_viewmodel
from ..service.agent_service import get_all_agents_with_order_by, get_agent_with_ability

api = agent_viewmodel.api
_agent = agent_viewmodel.agent
_ability = agent_viewmodel.ability


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


@api.route("/ability", strict_slashes=False)
class AgentList(Resource):
    @api.doc("Get random ability and picture of agent")
    @api.marshal_list_with(_ability)
    def get(self):
        args = request.args
        language = args.get("language")
        order_by_name = args.get("order_by_name")
        is_order = order_by_name == "true"

        return get_agent_with_ability(language, is_order)
