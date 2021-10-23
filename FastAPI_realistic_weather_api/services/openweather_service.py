from typing import Optional

import httpx

api_key: Optional[str] = None


async def get_report_async(city: str, state: Optional[str], country: str, units: str) -> dict:
    if state:
        q = f'{city},{state},{country}'
    else:
        q = f'{city},{country}'

    # Tutorial used a ? instead of a & before units in string below, I don't know why. Prob just a typo?
    # In 'Making an async API method' video it just changes to &, with no explanation I can find.
    # It is required to be a & for the request to work - ? gives an error.
    # url = f'https://api.openweathermap.org/data/2.5/weather?q={q}&appid={api_key}?units={units}'

    url = f'https://api.openweathermap.org/data/2.5/weather?q={q}&appid={api_key}&units={units}'

    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        resp.raise_for_status()

    data = resp.json()
    forecast = data['main']
    return forecast
