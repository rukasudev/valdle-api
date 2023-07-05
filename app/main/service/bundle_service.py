from util import get_by_valorant_api

import random


def _get_valorant_bundles(language: str) -> list:
    """Get all bundles from Valorant API"""

    response = get_by_valorant_api("bundles", language)

    # remove bundles without promo_image
    response.pop(36)
    response.pop(9)

    return response


def get_random_bundle_with_image(language: str) -> dict:
    """Get a random bundle with image and choices"""

    bundles = _get_valorant_bundles(language)
    choices = random.sample(bundles, 4)
    answer_bundle = random.choice(choices)

    return {
        "bundle_image": answer_bundle["verticalPromoImage"],
        "answer": answer_bundle["displayName"],
        "choices": [bundle["displayName"] for bundle in choices],
    }
