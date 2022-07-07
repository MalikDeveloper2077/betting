import aiohttp

from betmaker.core.settings import get_settings


base_url = get_settings().LINE_PROVIDER_DOMAIN


async def get_available_events() -> list:
    url = f'{base_url}/events'

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            return await resp.json()
