from ..config import Config

import requests


def get_by_valorant_api(path: str, language: str) -> str:
    query_param = f"?language={language}" if language else ""
    base_url = f"{Config.VALORANT_API}/{path}{query_param}"

    request = requests.get(base_url).json()
    response = request.get("data", dict())

    return response


def get_timezone_for_language(language):
    timezone_mapping = {
        "ar-AE": "Asia/Dubai",
        "de-DE": "Europe/Berlin",
        "en-US": "America/New_York",
        "es-ES": "Europe/Madrid",
        "es-MX": "America/Mexico_City",
        "fr-FR": "Europe/Paris",
        "id-ID": "Asia/Jakarta",
        "it-IT": "Europe/Rome",
        "ja-JP": "Asia/Tokyo",
        "ko-KR": "Asia/Seoul",
        "pl-PL": "Europe/Warsaw",
        "pt-BR": "America/Sao_Paulo",
        "ru-RU": "Europe/Moscow",
        "th-TH": "Asia/Bangkok",
        "tr-TR": "Europe/Istanbul",
        "vi-VN": "Asia/Ho_Chi_Minh",
        "zh-CN": "Asia/Shanghai",
        "zh-TW": "Asia/Taipei",
    }

    return timezone_mapping.get(language, "UTC")
