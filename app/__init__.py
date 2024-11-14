from fastapi import FastAPI

from .middlewares import BodyMiddleware
from .routes import api_router

app = FastAPI(debug=True)


app.add_middleware(BodyMiddleware)
app.include_router(api_router)
