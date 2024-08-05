# Router


class Router:
    def __init__(self):
        self.routes = {}

    def add_route(self, path, endpoint, methods):
        self.routes[path] = {"endpoint": endpoint, "methods": methods}

    def get_route(self, path, method):
        route = self.routes.get(path)
        if route and method in route["methods"]:
            return route["endpoint"]
        return None
