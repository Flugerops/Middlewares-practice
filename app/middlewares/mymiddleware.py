from typing import Awaitable, Callable

from fastapi import Request, Response, status
from starlette.middleware.base import (
    BaseHTTPMiddleware,
    DispatchFunction,
    RequestResponseEndpoint,
)
from starlette.types import ASGIApp


class HeadMiddleware(BaseHTTPMiddleware):
    def __init__(self, app: BaseHTTPMiddleware):
        super().__init__(app)

    async def dispatch(
        self, request: Request, call_next: Callable[[Request], Awaitable[Response]]
    ) -> Response:
        if "X-Custom-Header" not in request.headers:
            return Response("Missing Header", status_code=status.HTTP_400_BAD_REQUEST)
        response = await call_next(request)
        return response


class BodyMiddleware(HeadMiddleware):
    def __init__(self, app: BaseHTTPMiddleware):
        super().__init__(app)

    async def dispatch(
        self, request: Request, call_next: Callable[[Request], Awaitable[Response]]
    ) -> Response:

        response = await super().dispatch(request, call_next)

        # body = await request.json()
        # if "test" not in body:
        #     return Response("Missing Body", status_code=status.HTTP_400_BAD_REQUEST)
        response = await call_next(request)
        return response
