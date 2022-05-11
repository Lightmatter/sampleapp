# https://docs.djangoproject.com/en/4.0/topics/templates/#django.template.backends.jinja2.Jinja2

from django.templatetags.static import static
from django.urls import reverse
from jinja2 import Environment


def environment(**options):
    options.pop(
        "string_if_invalid", None
    )  # https://github.com/pytest-dev/pytest-django/issues/327
    env = Environment(autoescape=True, **options)
    env.globals.update(
        {
            "static": static,
            "url": reverse,
        }
    )
    return env
