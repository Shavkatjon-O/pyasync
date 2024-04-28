import asyncio

from httptools import HttpRequestParser

from http_parser import HttpParserMixin


class Server(asyncio.Protocol, HttpParserMixin):
    def __init__(self, loop):
        self._loop = loop
        self._encoding = "utf-8"
        self._url = None
        self._headers = {}
        self._body = None
        self._transport = None
        self._request_parser = HttpRequestParser(self)

    def connection_made(self, transport):
        self._transport = transport

    def connection_lost(self, *args):
        self._transport = None

    def data_received(self, data):
        # Pass data to our parser
        self._request_parser.feed_data(data)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    serv = Server(loop)
    server = loop.run_until_complete(loop.create_server(lambda: serv, port=8080))

    try:
        print("Started server on ::8080")
        loop.run_until_complete(server.serve_forever())
    except KeyboardInterrupt:
        server.close()
        loop.run_until_complete(server.wait_closed())
        loop.stop()
