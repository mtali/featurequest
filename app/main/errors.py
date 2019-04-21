from flask import render_template
from . import main

# template locations for error pages
PAGE_NOT_FOUND_TEMPLATE = "errors/404.html"
INTERNAL_SERVER_ERROR_TEMPLATE =  "errors/500.html"

@main.app_errorhandler(404)
def page_not_found(e):
    return render_template(PAGE_NOT_FOUND_TEMPLATE), 404


@main.app_errorhandler(500)
def internal_server_error(e):
    return render_template(INTERNAL_SERVER_ERROR_TEMPLATE), 500
