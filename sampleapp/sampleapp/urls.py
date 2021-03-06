from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

from django.contrib import admin

urlpatterns = [
    path("auth/", include("sampleapp.account.urls")),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.authtoken")),
    path("admin/", admin.site.urls),
    path("social/", include("social_django.urls", namespace="social")),
    path("backend/", include("sampleapp.home.urls")),
]
urlpatterns += [
    path("", include("sampleapp.wagtailapp.urls")),
]
if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    import debug_toolbar

    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [path(r"__debug__/", include(debug_toolbar.urls))]
