# Steve Triplett
# July 2021
# FastAPI Realistic Weather API

import fastapi
import uvicorn
from starlette.requests import Request
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

api = fastapi.FastAPI()
templates = Jinja2Templates('templates')
api.mount('/static', StaticFiles(directory='static'), name='static')


@api.get('/')
def index(request: Request):
    # return "Hello Weather App!"
    # return templates.TemplateResponse('home/index.html', {'request': request, 'other': [1,2,3]})
    return templates.TemplateResponse('home/index.html', {'request': request})


@api.get('/favicon.ico')
def favicon():
    return fastapi.responses.RedirectResponse(url='/static/img/test_favicon.ico')


@api.get('/api/weather')
def weather():
    return 'some report'



if __name__ == '__main__':
    uvicorn.run(api, port=8000, host='127.0.0.1')