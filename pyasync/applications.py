# Async Web Framework


class Pyasync:
    def __init__(self):
        self.routers = {}

    def route(self, path):
        def wrapper(handler):
            self.routers[path] = handler
            return handler

        return wrapper

    async def __call__(self, scope, receive, send):
        path = scope["path"]

        if path in self.routers:
            response = await self.routers[path](scope, receive, send)

            content_type = (
                "text/html" if response.startswith("<!DOCTYPE html>") else "text/plain"
            )

            await send(
                {
                    "type": "http.response.start",
                    "status": 200,
                    "headers": [
                        [b"content-type", content_type.encode()],
                    ],
                }
            )
            await send(
                {
                    "type": "http.response.body",
                    "body": response.encode("utf-8"),
                }
            )
        else:
            await send(
                {
                    "type": "http.response.start",
                    "status": 404,
                    "headers": [
                        [b"content-type", b"text/plain"],
                    ],
                }
            )
            await send(
                {
                    "type": "http.response.body",
                    "body": b"Not Found",
                }
            )
