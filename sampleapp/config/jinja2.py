# https://docs.djangoproject.com/en/4.0/topics/templates/#django.template.backends.jinja2.Jinja2

from django.templatetags.static import static
from django.urls import reverse
from django_vite.templatetags.django_vite import vite_asset, vite_hmr_client
from jinja2 import Environment

from sampleapp.config.settings.base import CSRF_COOKIE_NAME


def environment(**options):
    options.pop(
        "string_if_invalid", None
    )  # https://github.com/pytest-dev/pytest-django/issues/327
    # This actually works, the below is necessary for
    # flakeheaven env = Environment(**options)
    env = Environment(**options, autoescape=True)
    env.globals.update(
        {
            "static": static,
            "url": reverse,
            "csrf_cookie_name": CSRF_COOKIE_NAME,
            "vite_asset": vite_asset,
            "vite_hmr_client": vite_hmr_client,
        }
    )
    return env
