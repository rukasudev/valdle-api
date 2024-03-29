from ..config import Config
from typing import Dict

import requests
import random


def get_all_agents(language: str) -> list:
    """Get all agents of Valorant API"""

    query_param = f"&language={language}" if language else ""
    base_url = Config.VALORANT_API + f"/agents?isPlayableCharacter=true{query_param}"
    request = requests.get(base_url).json()
    response = list(request["data"])

    return response


def get_agent_by_index(index: int) -> Dict[str, str]:
    """(Source: Agents of Valorant API) Get agent by index"""

    request = get_all_agents()
    response = dict(request[index])
    return response


def get_all_agents_with_order_by(language: str, order_by_name: bool) -> Dict[str, str]:
    """(Optional: order by name) Get all agents from Valorant API"""

    agents = get_all_agents(language)
    response = []

    for agent in agents:
        agent_response = dict(
            uuid=agent["uuid"],
            agent_name=agent["displayName"],
            description=agent["description"],
            display_icon=agent["displayIcon"],
            portrait_banner=agent["fullPortrait"],
            background_banner=agent["background"],
            agent_colors=agent["backgroundGradientColors"],
        )
        response.append(agent_response)

    if order_by_name:
        return sorted(response, key=lambda item: item["agent_name"])

    return response, 200


def get_agent_with_ability(language: str, order_by_name: bool) -> Dict[str, str]:
    """Get agent with a ability"""
    requests = get_all_agents(language)

    random_agent = random.choice(requests)
    agent_name = random_agent["displayName"]
    agent_pic = random_agent["displayIcon"]

    ability = random_agent["abilities"]
    random_ability = random.choice(ability)
    ability_name = random_ability["displayName"]
    ability_pic = random_ability["displayIcon"]

    return {
        "agent_name": agent_name,
        "agent_picture": agent_pic,
        "ability_name": ability_name,
        "ability_picture": ability_pic,
    }
