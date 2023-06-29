import requests
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class _Params(BaseModel):
    headers: Optional[dict] = None
    methods: str = "get"
    url: str
    params: Optional[dict] = None
    data: Optional[dict] = None


@app.get("/")
def root():
    return {"App": "Proxy API"}


@app.post("/proxy-api/json")
def proxyAPI(item: _Params):
    methods = item.methods
    url = item.url
    params = item.params
    headers = item.headers
    data = item.data

    response = requests.request(
        method=methods, url=url, headers=headers, params=params, json=data
    )

    return response.json()
