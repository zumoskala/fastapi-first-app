from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI()

app.mount('/static', StaticFiles(directory='./tutorial/static'), name='static')
templates = Jinja2Templates(directory='./tutorial/templates')

from tutorial.views import main, tasks