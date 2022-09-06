from ..config import Config

import requests
import random


def get_all_bundles() -> list:
    """Get all bundles from Valorant API"""

    base_url = Config.VALORANT_API + "/bundles"
    request = requests.get(base_url).json()
    response = list(request["data"])

    # remove bundles without promo_image
    response.pop(9)
    response.pop(36)

    return response


def get_bundle_by_index(index: int) -> dict:
    """(Source: Bundles from Valorant API) Get bundle by index"""

    request = get_all_bundles()
    response = dict(request[index])
    return response


def get_random_bundle_with_image() -> dict:
    """Get a random bundle with image and choices"""

    bundles = get_all_bundles()
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

    answer_index = random.randint(0, len(choices) - 1)
    answer_bundle = bundles[answer_index]
    response = dict(
        bundle_image=answer_bundle["verticalPromoImage"],
        answer=answer_bundle["displayName"],
        choices=choices,
    )

    return response, 200
