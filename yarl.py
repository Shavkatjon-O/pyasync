import json

from yarl import URL


class Request:
    _encoding = "utf_8"

    def __init__(self, method, url, headers, version=None, body=None, app=None):
        self._version = version
        self._method = method.decode(self._encoding)
        self._url = URL(url.decode(self._encoding))
        self._headers = headers
        self._body = body

    @property
    def method(self):
        return self._method

    @property
    def url(self):
        return self._url

    @property
    def headers(self):
        return self._headers

    def text(self):
        if self._body is not None:
            return self._body.decode(self._encoding)

    def json(self):
        text = self.text()
        if text is not None:
            return json.loads(text)

    def __repr__(self):
        return f"<Request at 0x{id(self)}>"
