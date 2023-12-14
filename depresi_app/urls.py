from django.urls import path
from .views import *

urlpatterns = [
    path("", homescreen, name="home"),
    path("login/", custom_login, name="login"),
    path("logout/", custom_logout, name="logout"),
    # Dashboard
    path("dashboard/", dahsboard, name="dashboard"),
    path("user-history/", userhHistory, name="userhistory"),
    path("solusi/", solusi, name="solusi"),
    # Gejala Action
    path("gejala/", gejala, name="gejala"),
    path("tambah_gejala/", tambah_gejala, name="tambah_gejala"),
    path("edit_gejala/<int:gejala_id>/", edit_gejala, name="edit_gejala"),
    path("hapus_gejala/<int:gejala_id>/", hapus_gejala, name="hapus_gejala"),
    # Keterangan Action
    path("ket_pakar/", ketPakar, name="ket_pakar"),
    path("tambah_ket/", tambah_ket, name="tambah_ket"),
    path("edit_ket/<int:kode_keterangan>/", edit_ket, name="edit_ket"),
    path("hapus_ket/<int:kode_keterangan>/", hapus_ket, name="hapus_ket"),
    # Admin Action
    path("admin-list/", daftarAdmin, name="listadmin"),
    path("tambah_admin/", tambah_admin, name="tambah_admin"),
    path("edit_admin/<int:admin_id>/", edit_admin, name="edit_admin"),
    path("hapus_admin/<int:admin_id>/", hapus_admin, name="hapus_admin"),
    # PasienAction
    path("pasien-list/", userPasien, name="listpasien"),
    path("diagnosa/", handle_diagnosa, name="handle_diagnosa"),
]
