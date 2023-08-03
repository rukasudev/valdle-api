from flask import request
from flask_restx import Resource

from ..views import valdle_viewmodel
from ..service.valdle_service import check_word
from typing import Dict, Tuple

api = valdle_viewmodel.api
_valdle = valdle_viewmodel.valdle


@api.route("/verify_attempt")
class User(Resource):
    @api.expect(_valdle, validate=True)
    @api.doc("verify if the word is correctly")
    def post(self) -> Tuple[Dict[str, str], int]:
        language = request.args.get("language")
        attempt = request.get_json().get("attempt").lower()

        return check_word(attempt, language)
