from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
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
Keterangan VIEWS
keterangan views ini untuk membuat views bagian keterangan
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


"""
User Admin
User Admin views ini untuk membuat views bagian Admin
"""


def daftarAdmin(request):
    usrAdmin = User.objects.all()
    return render(request, "admin.html", {"user": request.user, "listAdmin": usrAdmin})


def tambah_admin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        # Cek apakah user dengan username tersebut sudah ada
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username sudah digunakan. Pilih username lain.")
            return redirect("tambah_admin")

        # Buat superuser
        user = User.objects.create_user(username, email, password)
        user.is_staff = True  # Tandai user sebagai staff/admin
        user.is_superuser = False  # Tandai user sebagai superuser
        user.save()

        messages.success(request, "Admin berhasil ditambahkan.")
        return redirect("listadmin")  # Ganti 'home' dengan nama url halaman utama Anda

    return render(request, "form_admin.html")


def edit_admin(request, admin_id):
    admin = get_object_or_404(User, id=admin_id)

    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        # Lakukan validasi data sesuai kebutuhan aplikasi
        if not username or not email or not password:
            # Handle kesalahan, misalnya kirim pesan kesalahan ke pengguna
            return render(
                request,
                "form_admin.html",
                {
                    "is_edit": True,
                    "admin": admin,
                    "error_message": "Semua bidang harus diisi.",
                },
            )

        # Lakukan sesuatu dengan data yang diterima, seperti menyimpan ke database
        admin.username = username
        admin.email = email
        admin.password = password
        admin.save()

        return redirect("listadmin")  # Ganti 'nama_view' dengan view yang sesuai

    return render(request, "form_admin.html", {"is_edit": True, "admin": admin})


def hapus_admin(request, admin_id):
    admin = get_object_or_404(User, id=admin_id)
    admin.delete()
    return redirect("listadmin")


# USER
# Disini untuk fungsi user
def userPasien(request):
    user = UserPasien.objects.all()
    return render(request, "pasien.html", {"user": request.user, "listPasien": user})


from django.shortcuts import render, redirect
from .models import UserPasien, Gejala, Keterangan


def handle_diagnosa(request):
    if request.method == "POST":
        nama = request.POST.get("nama")
        jurusan = request.POST.get("jurusan")

        # Membuat objek UserPasien
        user_pasien = UserPasien.objects.create(nama=nama, jurusan=jurusan)

        # Mengambil data gejala dan bobot dari formulir
        for gejala in Gejala.objects.all():
            kode_gejala = gejala.kode_gejala
            bobot = request.POST.get(f"gejala_{kode_gejala}")

            # Menyimpan data ke model UserPasien
            setattr(user_pasien, f"p1_{kode_gejala}", bobot)
            setattr(user_pasien, f"p2_{kode_gejala}", bobot)
            setattr(user_pasien, f"p3_{kode_gejala}", bobot)

        # Menyimpan data ke model UserPasien
        user_pasien.save()

        return redirect(
            "home"
        )  # Ganti 'hasil_diagnosa' dengan nama view hasil diagnosa

    # Jika bukan POST, tampilkan formulir
    return render(
        request,
        "diagnosa.html",
        {
            "gejala_list": Gejala.objects.all(),
            "keterangan_list": Keterangan.objects.all(),
        },
    )
