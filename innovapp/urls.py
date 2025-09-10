from django.contrib import admin
from django.urls import path
from . import views as v

urlpatterns = [
    path("", v.home),
    path('aboutus',v.aboutus),
    path('services',v.services),
]
