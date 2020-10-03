from tutorial import app, templates
from fastapi import Request

@app.get("/")
async def index(request : Request):
    return templates.TemplateResponse("index.html", {"request" : request})

@app.get("/tutorial")
async def tutorial():
    return {"message" : {"this is another route"}}
