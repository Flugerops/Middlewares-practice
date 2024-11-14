# from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
# from fastapi import Request, Response, FastAPI, status
# from typing import Awaitable, Callable


# class HeaderMiddleware(BaseHTTPMiddleware):
#     def __init__(self, app: BaseHTTPMiddleware, header_ignore: str):
#         super().__init__(app)
#         self.header_ignore = header_ignore

#     async def dispatch(
#         self, request: Request, call_next: RequestResponseEndpoint
#     ) -> Response:
#         if request.headers.get(self.header_ignore):
#             return Response(status_code=status.HTTP_403_FORBIDDEN)

#         responce = await call_next(request)
#         return responce


# class BodyMiddleware(BaseHTTPMiddleware):
#     def __init__(self, app: BaseHTTPMiddleware, content_ignore: str):
#         super().__init__(app)
#         self.content_ignore = content_ignore

#     async def dispatch(
#         self, request: Request, call_next: RequestResponseEndpoint
#     ) -> Response:
#         responce = await call_next(request)

#         if
