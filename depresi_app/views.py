from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import *


def homescreen(request):
    return render(request, "home.html", {"user": request.user})


def custom_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect("home")
        else:
            # Return an 'invalid login' error message.
            return render(
                request,
                "login.html",
                {"error_message": "Invalid login credentials"},
            )

    return render(request, "login.html")


def custom_logout(request):
    logout(request)
    # Redirect ke halaman setelah logout
    return redirect("home")  # Ganti 'home' dengan nama URL tujuan setelah logout


# INI UNTUK DASHBOARD
def dahsboard(request):
    return render(request, "dashboard.html", {"user": request.user})


def daftarAdmin(request):
    return render(request, "admin.html", {"user": request.user})


def userhHistory(request):
    return render(request, "userhistory.html", {"user": request.user})


def solusi(request):
    return render(request, "solusi.html", {"user": request.user})


"""
GEJALA VIEWS
gejala views ini untuk membuat views bagian gejala
"""


def gejala(request):
    # Mengambil semua data dari model Gejala
    gejala_list = Gejala.objects.all()
    return render(
        request, "gejala.html", {"user": request.user, "gejala_list": gejala_list}
    )


def tambah_gejala(request):
    if request.method == "POST":
        kode_gejala = request.POST.get("kode_gejala")
        keterangan_gejala = request.POST.get("keterangan_gejala")
        p1 = request.POST.get("p1")
        p2 = request.POST.get("p2")
        p3 = request.POST.get("p3")

        # Lakukan sesuatu dengan data yang diterima, seperti menyimpan ke database
        gejala = Gejala(
            kode_gejala=kode_gejala,
            keterangan_gejala=keterangan_gejala,
            p1=p1,
            p2=p2,
            p3=p3,
        )
        gejala.save()

        return redirect("gejala")  # ganti 'nama_view' dengan view yang sesuai

    return render(request, "form_gejala.html", {"is_edit": False})


def edit_gejala(request, gejala_id):
    gejala = get_object_or_404(Gejala, id=gejala_id)

    if request.method == "POST":
        kode_gejala = request.POST.get("kode_gejala")
        keterangan_gejala = request.POST.get("keterangan_gejala")
        p1 = request.POST.get("p1")
        p2 = request.POST.get("p2")
        p3 = request.POST.get("p3")

        # Lakukan validasi data sesuai kebutuhan aplikasi
        if not kode_gejala or not keterangan_gejala or not p1 or not p2 or not p3:
            # Handle kesalahan, misalnya kirim pesan kesalahan ke pengguna
            return render(
                request,
                "form_gejala.html",
                {
                    "is_edit": True,
                    "gejala": gejala,
                    "error_message": "Semua bidang harus diisi.",
                },
            )

        # Lakukan sesuatu dengan data yang diterima, seperti menyimpan ke database
        gejala.kode_gejala = kode_gejala
        gejala.keterangan_gejala = keterangan_gejala
        gejala.p1 = p1
        gejala.p2 = p2
        gejala.p3 = p3
        gejala.save()

        return redirect("gejala")  # Ganti 'nama_view' dengan view yang sesuai

    return render(request, "form_gejala.html", {"is_edit": True, "gejala": gejala})


def hapus_gejala(request, gejala_id):
    gejala = get_object_or_404(Gejala, id=gejala_id)
    gejala.delete()
    return redirect("gejala")


# Create your views here.


"""
GEJALA VIEWS
gejala views ini untuk membuat views bagian gejala
"""


def ketPakar(request):
    # Keterangan.objects.all().delete()
    ket_list = Keterangan.objects.all()
    return render(
        request, "ket_pakar.html", {"user": request.user, "ket_list": ket_list}
    )


def tambah_ket(request):
    if request.method == "POST":
        keterangan = request.POST.get("keterangan")
        cf = request.POST.get("cf")

        # Lakukan sesuatu dengan data yang diterima, seperti menyimpan ke database
        ket = Keterangan(
            keterangan=keterangan,
            cf=cf,
        )
        ket.save()

        return redirect("ket_pakar")  # ganti 'nama_view' dengan view yang sesuai

    return render(request, "form_ket.html", {"is_edit": False})


def edit_ket(request, kode_keterangan):
    ket = get_object_or_404(Keterangan, kode_keterangan=kode_keterangan)

    if request.method == "POST":
        keterangan = request.POST.get("keterangan")
        cf = request.POST.get("cf")

        # Lakukan validasi data sesuai kebutuhan aplikasi
        if not keterangan or not cf:
            # Handle kesalahan, misalnya kirim pesan kesalahan ke pengguna
            return render(
                request,
                "form_ket.html",
                {
                    "is_edit": True,
                    "keterangan": ket,
                    "error_message": "Semua bidang harus diisi.",
                },
            )

        # Lakukan sesuatu dengan data yang diterima, seperti menyimpan ke database
        ket.keterangan = keterangan
        ket.cf = cf
        ket.save()

        return redirect("ket_pakar")  # Ganti 'nama_view' dengan view yang sesuai

    return render(request, "form_ket.html", {"is_edit": True, "keterangan": ket})


def hapus_ket(request, kode_keterangan):
    ket = get_object_or_404(Keterangan, kode_keterangan=kode_keterangan)
    ket.delete()
    return redirect("ket_pakar")
