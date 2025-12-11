from django.urls import path
from .views import about,contact,login,home

urlpatterns = [
    path("about/",about),
    path("contact/",contact),
    path("login/",login),
    path("home/",home)
]
