from .util import get_by_valorant_api, get_timezone_for_language
from collections import Counter

import random
import datetime
import pytz

CATEGORIES = ["agents", "bundles", "gamemodes", "maps", "weapons", "skins"]
RANDOM_WORDS_OF_THE_DAY = {}
LAST_GENERATION_DATES = {}


def get_random_word(category, language):
    response = get_by_valorant_api(category, language)
    random_item = random.choice(filter_response(response, language))

    return random_item


def filter_response(response, language):
    word_of_the_day = RANDOM_WORDS_OF_THE_DAY.get(language)
    min_length, max_length = 3, 6

    return [
        item["displayName"]
        for item in response
        if min_length <= len(item["displayName"]) <= max_length
        and item["displayName"] != word_of_the_day
    ]


def generate_random_word_of_the_day(language):
    global RANDOM_WORDS_OF_THE_DAY, LAST_GENERATION_DATES

    language_timezone = get_timezone_for_language(language)

    now = datetime.datetime.now(pytz.timezone(language_timezone))
    today = now.date()

    if (
        language in LAST_GENERATION_DATES
        and LAST_GENERATION_DATES[language] == today
        and language in RANDOM_WORDS_OF_THE_DAY
    ):
        return RANDOM_WORDS_OF_THE_DAY[language]

    category = random.choice(CATEGORIES)
    category = "weapons/skins" if category == "skins" else category
    RANDOM_WORDS_OF_THE_DAY[language] = get_random_word(category, language).lower()
    LAST_GENERATION_DATES[language] = today

    return RANDOM_WORDS_OF_THE_DAY[language]


def check_word(attempt, language="en-US"):
    word_of_the_day = generate_random_word_of_the_day(language)

    if len(attempt) != len(word_of_the_day):
        return {"error": f"The attempt must have {len(word_of_the_day)} letters."}, 422

    if attempt == word_of_the_day:
        return {"is_correct": True, "word": attempt}

    word_of_the_day_counter = Counter(word_of_the_day)
    feedback = []

    for a, w in zip(attempt, word_of_the_day):
        if a == w:
            feedback.append({"color_code": 2, "letter": a})
            word_of_the_day_counter[w] -= 1
        elif word_of_the_day_counter[a] > 0:
            feedback.append({"color_code": 1, "letter": a})
            word_of_the_day_counter[a] -= 1
        else:
            feedback.append({"color_code": 0, "letter": a})

    return {"is_correct": False, "feedback": feedback}
