"""
Example options from the docs
options = {
    "tests": {
        "mytest": "path.to.tests.mytestfn",
    },
    "filters": {
        "myfilter": "path.to.filters.myfilterfn",
    },
    "constants": {
        "hello": "hello world",
    },
    "globals": {
        "somefn": "path.to.functions.somefn",
    },
}
"""
import datetime

options = {
    "constants": {"csrf_cookie_name": "sampleapp"},
    "filters": {
        "template_localtime": "django.utils.timezone.template_localtime",
    },
    "globals": {
        "vite_asset": "django_vite.templatetags.django_vite.vite_asset",
        "vite_hmr_client": "django_vite.templatetags.django_vite.vite_hmr_client",
        "django_htmx_script": "django_htmx.templatetags.django_htmx.django_htmx_script",
        "now": datetime.datetime.utcnow,
        "template_localtime": "django.utils.timezone.template_localtime",
    },
}
