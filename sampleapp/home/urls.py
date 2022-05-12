from django.urls import path
from django.views.generic.base import TemplateView

from .views import current_time, error

urlpatterns = [
    path("jinja/", TemplateView.as_view(template_name="jinja.jinja"), name="jinja"),
    path("jinja2/", TemplateView.as_view(template_name="jinja2.jinja"), name="jinja2"),
    path(r"current-time/", current_time, name="current_time"),
    path(r"error/", error, name="error"),
    path(r"", TemplateView.as_view(template_name="index.jinja"), name="home"),
]
