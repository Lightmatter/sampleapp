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
import random
from math import ceil, floor


def random_chart(
    num_times: int = 10, num_vars: int = 2, starting_val: int = 100
) -> list[list[int]]:
    results = [[starting_val for i in range(num_vars)]]
    for _time in range(num_times - 1):
        previous_mean = sum(results[-1]) / num_vars
        results.append([])
        for var in range(num_vars):
            previous_val = (results[-2][var] + previous_mean) / 2
            results[-1].append(
                random.randrange(  # noqa
                    floor(0.67 * previous_val), ceil(1.5 * previous_val)  # noqa
                )  # noqa
            )
    return results


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
        "random_chart": random_chart,
    },
}
