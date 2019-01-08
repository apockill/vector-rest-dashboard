import falcon
from falcon import Response
from jinja2 import Template

from .paths import STATIC_DIR


def load_template(template_name: str) -> Template:
    """
    :param template_name: The filename of the template. E.g. index.html
    """
    path = (STATIC_DIR / template_name).absolute()

    # Validate the template exists
    if not path.is_file():
        raise FileNotFoundError(
            f"Could not find the template {path} on the server!")

    with open(path, 'r') as f:
        return Template(f.read())


def respond_with_remplate(template_name, resp: Response):
    """Load a template using jinja2 and fill out the falcon response with
    said template (including the expected content type"""
    template = load_template(template_name)
    resp.status = falcon.HTTP_200
    resp.content_type = "text/html"
    resp.body = template.render()
    return resp
