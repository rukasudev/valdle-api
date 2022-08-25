import requests
import json
import random


def get_random_bundle_with_image():
    response = requests.get("https://valorant-api.com/v1/bundles").json()
    bundles = response["data"]
    random_number = random.randint(0, len(bundles) - 1)
    random_bundle = bundles[random_number]
    bundle_name = random_bundle["displayName"]
    bundle_image = random_bundle["verticalPromoImage"]
    bundle_with_image = dict(bundle_name=bundle_name, bundle_image=bundle_image)
    return bundle_with_image, 200
