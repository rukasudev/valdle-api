import requests
import json
import random


def get_random_bundle_with_image():
    response = requests.get("https://valorant-api.com/v1/bundles").json()
    bundles = response["data"]
    list_op = []
    response = {}
    black_list = [9, 36]
    random_number = random.randint(0, len(bundles) - 1)
    random_bundle = bundles[random_number]
    while random_number in black_list:
        random_number = random.randint(0, len(bundles) - 1)

    bundle_name = random_bundle["displayName"]
    response["answer"] = bundle_name
    list_op.append(bundle_name)
    bundle_image = random_bundle["verticalPromoImage"]
    response["bundle_image"] = bundle_image

    for i in range(1, 4):

        random_number2 = random.randint(0, len(bundles) - 1)
        random_op = bundles[random_number2]
        op_bundle = random_op["displayName"]
        while op_bundle in list_op:
            random_number2 = random.randint(0, len(bundles) - 1)

        op_bundle = random_op["displayName"]
        list_op.append(op_bundle)
    random.shuffle(list_op)
    response["choices"] = list_op
    return response, 200
