from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("api/", include("kakao_api_hook.urls")),
]
