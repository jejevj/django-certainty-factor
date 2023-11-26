from django.urls import path
from .views import *

urlpatterns = [
    path("", homescreen, name="home"),
    path("login/", custom_login, name="login"),
    path("logout/", custom_logout, name="logout"),
    # Dashboard
    path("dashboard/", dahsboard, name="dashboard"),
    path("ket_pakar/", ketPakar, name="ket_pakar"),
    path("admin-list/", daftarAdmin, name="listadmin"),
    path("user-history/", userhHistory, name="userhistory"),
    path("solusi/", solusi, name="solusi"),
    path("gejala/", gejala, name="gejala"),
]
