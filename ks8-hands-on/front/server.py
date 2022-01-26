from urllib import request
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import uvicorn
import requests

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/")
def  home(request:Request):
    return templates.TemplateResponse("index.html",{"request":request})

@app.post("/test_request")
def test_request(request:Request):
    r = requests.get('http://127.0.0.1:4001')
    return(r.content)

# if __name__ == "__main__":
#     uvicorn.run("server:app", host="127.0.0.1", port=4000, log_level="info")    