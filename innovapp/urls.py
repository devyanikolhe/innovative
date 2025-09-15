from django.contrib import admin
from django.urls import path
from . import views as v

urlpatterns = [
    path("", v.home),
    path('aboutus/',v.aboutus,name="aboutus"),
    path('services/',v.services,name="services"),
    path('contact/',v.contact,name="contact"),
    path('appointment/',v.appointment,name="appointment"),
    path("login/", v.login_view, name="login"),
    path("register/", v.register_view, name="register"),
    path("logout/",v.logout_view,name="logout")
]
