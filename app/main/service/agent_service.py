from ..config import Config

import requests


def get_all_agents(language: str) -> list:
    """Get all agents of Valorant API"""

    query_param = f"&language={language}" if language else ""
    base_url = Config.VALORANT_API + f"/agents?isPlayableCharacter=true{query_param}"
    request = requests.get(base_url).json()
    response = list(request["data"])

    return response


def get_agent_by_index(index: int) -> dict:
    """(Source: Agents of Valorant API) Get agent by index"""

    request = get_all_agents()
    response = dict(request[index])
    return response


def get_all_agents_with_order_by(language: str, order_by_name: bool) -> dict:
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
