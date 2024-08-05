# Response


class Response:
    def __init__(self, content, status_code=200, headers=None):
        self.content = content
        self.status_code = status_code
        self.headers = headers or []

    async def __call__(self, scope, receive, send):
        await send(
            {
                "type": "http.response.start",
                "status": self.status_code,
                "headers": [
                    (
                        b"content-type",
                        b"text/plain",
                    )
                ]
                + self.headers,
            }
        )
        await send(
            {
                "type": "http.response.body",
                "body": self.content.encode("utf-8"),
            }
        )
