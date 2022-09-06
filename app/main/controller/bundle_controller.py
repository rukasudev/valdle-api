from flask import request
from flask_restx import Resource

from ..util.dto import BundleDto
from ..service.bundle_service import get_random_bundle_with_image
from typing import Dict, Tuple

api = BundleDto.api
_bundle = BundleDto.bundle


@api.route("/random")
class BundleList(Resource):
    @api.doc("return a random bundle with image")
    @api.marshal_list_with(_bundle)
    def get(self):
        return get_random_bundle_with_image()
