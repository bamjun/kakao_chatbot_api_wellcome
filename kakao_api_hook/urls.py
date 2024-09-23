from django.urls import path

from .views import Test_api

urlpatterns = [
    path("", Test_api.as_view()),
]
