from fastapi import FastAPI, APIRouter, Request, Response
from fastapi.responses import JSONResponse, RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional
from pydantic import BaseSettings

# from metrics import router
from api import metrics_api


api_router = APIRouter()

# Import tests from the metrics folder:
# api_router.include_router(metrics_api.router, prefix='/tests', tags=["FAIR Metrics Tests"])
api_router.include_router(metrics_api.router, prefix='/tests')

app = FastAPI(
    title='FAIR Metrics tests API for Rare Disease',
    description="""FAIR Metrics tests API for resources related to research on Rare Disease.

[Source code](https://github.com/MaastrichtU-IDS/fair-enough-metrics)    
""",
    license_info = {
        "name": "MIT license",
        "url": "https://opensource.org/licenses/MIT"
    },
    contact = {
        "name": "Vincent Emonet",
        "email": "vincent.emonet@gmail.com",
        "url": "https://github.com/vemonet",
    },
)

app.include_router(api_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", include_in_schema=False)
def redirect_root_to_docs():
    """Redirect the route / to /docs"""
    return RedirectResponse(url='/docs')
