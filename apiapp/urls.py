from django.urls import path

from . import views
from .views import TestApiView

urlpatterns = [
    path("test", TestApiView.as_view()),
]
