from typing import Annotated
import logging

from fastapi import APIRouter, Header

from ..middlewares import logger

# from ..schemas import Header


api_router = APIRouter(prefix="/api")

# def setup_middleware():
#     api_router.add_middleware()


@api_router.get("/")
async def home():
    return {"Hello": "World"}


@api_router.post("/create_thing")
async def create_thing():
    return {"Test": "Message"}


@api_router.post("/")
async def home(X_Custom_Header: Annotated[str | None, Header()] = None):
    return {"header": X_Custom_Header}
