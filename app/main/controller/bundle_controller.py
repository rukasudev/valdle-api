from flask import request
from flask_restx import Resource

from ..util.dto import BundleDto
from ..service.bundle_service import get_random_bundle_with_image
from typing import Dict, Tuple

api = BundleDto.api
_bundle = BundleDto.bundle


@api.route("/")
class UserList(Resource):
    @api.doc("retorna um bundle aleatorio")
    @api.marshal_list_with(_bundle, envelope="data")
    def get(self):
        """retorna um bundle aleatorio"""
        return get_random_bundle_with_image()
