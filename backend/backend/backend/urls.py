"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.urls import path, include
from django.http import HttpResponse
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

schema_view = get_schema_view(
    openapi.Info(
        title="EconPlaza API",
        default_version="v1",
        description="This is the documentation for the EconPlaza API",
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    re_path(
        r"^docs/$", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"
    ),
    path("v1/users/", include("accounts.urls")),
    path("admin/", admin.site.urls),
    path("v1/auth/login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("v1/auth/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("v1/plazas/", include("plazas.urls.plazas")),
    path("v1/posts/", include("plazas.urls.posts")),
    path("v1/tags/", include("plazas.urls.tags")),
    path(
        "",
        lambda _: HttpResponse(
            '<div style="max-width: 400px;font-family: Helvetica, Sans-Serif;font-size: 1.2em;margin: 20vh '
            'auto;"><p>"Programming today is a race between software engineers striving to build bigger and better '
            "idiot-proof programs, and the Universe trying to produce bigger and better idiots. So far, the Universe is "
            'winning."</p><p>- <em>Rick Cook, The Wizardry Compiled</em></p></div>',
            headers={"content-type": "text/html"},
            status=200,
        ),
    ),
]
