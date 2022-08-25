from app.main import db

from app.main.model.blacklist import BlacklistToken
from typing import Dict, Tuple


def save_token(token: str) -> Tuple[Dict[str, str], int]:
    blacklist_token = BlacklistToken(token=token)
    try:
        db.session.add(blacklist_token)
        db.session.commit()
        response_object = {"status": "success", "message": "Successfully logged out."}
        return response_object, 200
    except Exception as error:
        response_object = {"status": "fail", "message": error}
        return response_object, 200
