from flask import request
from flask_restx import Resource

from ..views import bundle_viewmodel
from ..service.bundle_service import get_random_bundle_with_image

api = bundle_viewmodel.api
_bundle = bundle_viewmodel.bundle


@api.route("/random")
class BundleList(Resource):
    @api.doc("return a random bundle with image")
    @api.marshal_list_with(_bundle)
    def get(self):
        args = request.args
        language = args.get("language")

        return get_random_bundle_with_image(language)
