from django.urls import path
from . import views

urlpatterns = [
    path('', views.hellow),
    path("about/", views.about),
]