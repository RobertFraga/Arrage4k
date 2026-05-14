from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('not-found', views.notFound, name="not-found"),
]