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
    # Gejala Action
    path("tambah_gejala/", tambah_gejala, name="tambah_gejala"),
    path("edit_gejala/<int:gejala_id>/", edit_gejala, name="edit_gejala"),
    path("hapus_gejala/<int:gejala_id>/", hapus_gejala, name="hapus_gejala"),
    # Keterangan Action
    path("tambah_ket/", tambah_ket, name="tambah_ket"),
    path("edit_ket/<int:kode_keterangan>/", edit_ket, name="edit_ket"),
    path("hapus_ket/<int:kode_keterangan>/", hapus_ket, name="hapus_ket"),
]
