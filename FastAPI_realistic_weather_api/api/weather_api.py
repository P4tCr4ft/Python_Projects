from typing import Optional

import fastapi

router = fastapi.APIRouter()


@router.get('/api/weather/{city}')
def weather(city: str,
            country: str,
            state: Optional[str] = None,
            # country: str = 'US',
            units: Optional[str] = 'metric'):
    # return 'Some report for ' + city
    return f"{city}, {state}, {country} in {units}"
