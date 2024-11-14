import logging
from fastapi import APIRouter

from ..middlewares import logger

# from ..schemas import Header


api_router = APIRouter(prefix="/api")

# def setup_middleware():
#     api_router.add_middleware()


@api_router.get("/")
async def index():
    return {"Test": "Message"}
