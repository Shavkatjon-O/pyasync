import uvicorn

from pyasync.applications import Pyasync
from pyasync.responses import Response


app = Pyasync()


async def home_page():
    return Response("Hello, World!")


app.add_route("/", home_page, methods=["GET"])


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
