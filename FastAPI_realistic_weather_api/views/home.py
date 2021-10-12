import fastapi

from starlette.requests import Request
from starlette.templating import Jinja2Templates

router = fastapi.APIRouter()
templates = Jinja2Templates('templates')


@router.get('/')
def index(request: Request):
    # return "Hello Weather App!"
    # return templates.TemplateResponse('home/index.html', {'request': request, 'other': [1,2,3]})
    return templates.TemplateResponse('home/index.html', {'request': request})


@router.get('/favicon.ico')
def favicon():
    return fastapi.responses.RedirectResponse(url='/static/img/test_favicon.ico')
