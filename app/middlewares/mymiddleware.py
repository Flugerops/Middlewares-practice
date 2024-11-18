from typing import Awaitable, Callable

from fastapi import Request, Response, status, FastAPI
from starlette.middleware.base import (
    BaseHTTPMiddleware,
    DispatchFunction,
    RequestResponseEndpoint,
)
from starlette.types import ASGIApp


class HeadMiddleware(BaseHTTPMiddleware):
    def __init__(
        self,
        app: ASGIApp,
        head_ignore: set[str] = set(),
    ):
        super().__init__(app)
        self.head_ignore = head_ignore

    async def dispatch(
        self, request: Request, call_next: Callable[[Request], Awaitable[Response]]
    ) -> Response:

        if not request.url.path in self.head_ignore:
            if "X-Custom-Header" not in request.headers:
                return Response(
                    "Missing Header", status_code=status.HTTP_400_BAD_REQUEST
                )
        response = await call_next(request)
        return response


class BodyMiddleware(HeadMiddleware):
    def __init__(
        self, app: ASGIApp, head_ignore: set[str] = set(), body_ignore: set[str] = set()
    ):
        super().__init__(app, head_ignore)
        self.body_ignore = body_ignore

    async def dispatch(
        self, request: Request, call_next: Callable[[Request], Awaitable[Response]]
    ) -> Response:
        if request.method == "POST":
            body = {}
            try:
                body = await request.json()
            except Exception:
                if request.url.path not in self.body_ignore:
                    return Response(
                        "Invalid or missing JSON Body", 
                        status_code=status.HTTP_400_BAD_REQUEST
                    )
            
            if request.url.path not in self.body_ignore and "name" not in body:
                return Response(
                    "Missing 'name' in JSON body", 
                    status_code=status.HTTP_400_BAD_REQUEST
                )
        
        response = await super().dispatch(request, call_next)
        return response