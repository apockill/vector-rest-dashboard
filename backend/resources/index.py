from backend.templates import respond_with_remplate


class IndexResource:
    def on_get(self, req, resp):
        respond_with_remplate("index.html", resp)
