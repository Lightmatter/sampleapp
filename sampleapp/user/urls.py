from django.urls import path

from .views import login, signup, user_redirect_view, welcome

app_name = "user"
urlpatterns = [
    path("login/", view=login, name="account__login"),
    path("signup/", view=signup, name="account__signup"),
    path("welcome/", view=welcome, name="account__welcome"),
    path("~redirect/", view=user_redirect_view, name="redirect"),
]
