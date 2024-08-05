from pyasync.routing import Router
from pyasync.responses import Response


class Pyasync:
    def __init__(self):
        self.router = Router()

    def add_route(self, path, endpoint, methods=["GET"]):
        self.router.add_route(path, endpoint, methods)

    async def __call__(self, scope, receive, send):
        assert scope["type"] == "http"

        path = scope["path"]
        method = scope["method"]

        handler = self.router.get_route(path, method)

        if handler:
            response = await handler()
        else:
            response = Response("Not Found", status_code=404)

        await response(scope, receive, send)
