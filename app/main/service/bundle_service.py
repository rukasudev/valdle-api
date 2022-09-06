from ..config import Config

import requests
import random


def get_all_bundles(language: str) -> list:
    """Get all bundles from Valorant API"""

    query_param = f"?language={language}" if language else ""
    base_url = Config.VALORANT_API + f"/bundles{query_param}"
    request = requests.get(base_url).json()
    response = list(request["data"])

    # remove bundles without promo_image
    response.pop(36)
    response.pop(9)

    return response


def get_bundle_by_index(index: int) -> dict:
    """(Source: Bundles from Valorant API) Get bundle by index"""

    request = get_all_bundles()
    response = dict(request[index])
    return response


def get_random_bundle_with_image(language: str) -> dict:
    """Get a random bundle with image and choices"""

    bundles = get_all_bundles(language)
    choices = []
    choices_index = []

    while len(choices) < 4:
        sorted_index = random.randint(0, len(bundles) - 1)
        if sorted_index in choices_index:
            continue

        random_bundle = bundles[sorted_index]
        display_name = random_bundle["displayName"]
        choices_index.append(sorted_index)
        choices.append(display_name)

    answer_index = random.choice(choices_index)
    answer_bundle = bundles[answer_index]
    response = dict(
        bundle_image=answer_bundle["verticalPromoImage"],
        answer=answer_bundle["displayName"],
        choices=choices,
    )

    return response, 200
