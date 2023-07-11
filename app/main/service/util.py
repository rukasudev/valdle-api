from ..config import Config

import requests

def get_by_valorant_api(path: str, language: str) -> str:
    query_param = f"?language={language}" if language else ""
    base_url = f"{Config.VALORANT_API}/{path}{query_param}"
    
    request = requests.get(base_url).json()
    response = request.get("data", dict())
    
    return response
