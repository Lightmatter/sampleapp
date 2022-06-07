from django.urls import path
from django.views.generic.base import TemplateView

from .views import current_time, error

urlpatterns = [
    path(r"current-time/", current_time, name="current_time"),
    path(
        "random-chart/",
        TemplateView.as_view(template_name="random_chart.jinja"),
        name="random_chart",
    ),
    path(
        "components/",
        TemplateView.as_view(template_name="components.jinja"),
        name="components",
    ),
    path(r"error/", error, name="error"),
    path(r"", TemplateView.as_view(template_name="index.jinja"), name="home"),
]
