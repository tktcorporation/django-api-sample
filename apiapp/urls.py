from .views import TestApiView
from django.urls import path
from . import views

urlpatterns = [
    path('test', TestApiView.as_view()),
]