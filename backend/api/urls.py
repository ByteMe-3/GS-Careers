from django.urls import path

from .views import Example

urlpatterns = [
    path("example/", Example.as_view()),
]
