from fastapi import FastAPI

from .middlewares import BodyMiddleware
from .routes import api_router, home

app = FastAPI(debug=True)


app.add_middleware(
    BodyMiddleware, head_ignore={"/docs", "/api"}, body_ignore={"/docs", "/api"}
)
app.include_router(api_router)
