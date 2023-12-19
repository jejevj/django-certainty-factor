from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse
from .models import *
from .example_cf import *
import ast


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
      # Logika untuk menampilkan halaman detail diagnosa berdasarkan kode_pasien
    
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
def userPasien(request):
    user_pasiens = UserPasien.objects.all()

    # Assuming 'p1', 'p2', 'p3', and 'cf' are fields in the UserPasien model
    per1_list = []
    per2_list = []
    per3_list = []

    for user_pasien in user_pasiens:
        a_list = ast.literal_eval(user_pasien.p1)
        p1_list = [float(elem) for elem in a_list]
        b_list = ast.literal_eval(user_pasien.p2)
        p2_list = [float(elem) for elem in b_list]
        c_list = ast.literal_eval(user_pasien.p3)
        p3_list = [float(elem) for elem in c_list]
        d_list = ast.literal_eval(user_pasien.cf)
        cf_list = [float(elem) for elem in d_list]

        # Filter nilai 0
        filtered_p1, filtered_cf1 = filter_nonzero_values(p1_list, cf_list)
        filtered_p2, filtered_cf2 = filter_nonzero_values(p2_list, cf_list)
        filtered_p3, filtered_cf3 = filter_nonzero_values(p3_list, cf_list)

        combined_cf1 = calculate_combined_cf(filtered_p1, filtered_cf1)
        percentage_cf1 = combined_cf1 * 100
        combined_cf2 = calculate_combined_cf(filtered_p2, filtered_cf2)
        percentage_cf2 = combined_cf2 * 100
        combined_cf3 = calculate_combined_cf(filtered_p3, filtered_cf3)
        percentage_cf3 = combined_cf3 * 100

        # Append the percentages to the lists
        per1_list.append(percentage_cf1)
        per2_list.append(percentage_cf2)
        per3_list.append(percentage_cf3)

    context = {
        "user": request.user,
        "listPasien": user_pasiens,
        'per3': per3_list,
        'per2': per2_list,
        'per1': per1_list,
    }

    return render(request, "pasien.html", context)


from django.shortcuts import render, redirect
from .models import UserPasien, Gejala, Keterangan


def handle_diagnosa(request):
    if request.method == 'POST':
        nama = request.POST.get('nama')
        kode_pasien = request.POST.get('kode_pasien')
        jurusan = request.POST.get('jurusan')
        listGejala = []
        listP1 = []
        listP2 = []
        listP3 = []
        listCF = []

        # Lakukan penyimpanan data UserPasien di database
        for gejala in Gejala.objects.all():
            p1 = gejala.p1
            p2 = gejala.p2
            p3 = gejala.p3
            gejala_key = f'gejala_{gejala.kode_gejala}'
            keterangan_value = request.POST.get(gejala_key)
            listGejala.append(gejala.kode_gejala)
            listP1.append(p1)
            listP2.append(p2)
            listP3.append(p3)
            listCF.append(keterangan_value)

        user_pasien = UserPasien.objects.create(
            kode_pasien=kode_pasien,
            nama=nama,
            jurusan=jurusan,
            kode_gejala=str(listGejala),
            p1=str(listP1),
            p2=str(listP2),
            p3=str(listP3),
            cf=str(listCF)
        )

        # Menggunakan reverse untuk mendapatkan URL dengan nama 'detail_diagnosa' dan parameter 'kode_pasien'
        detail_diagnosa_url = reverse('detail_diagnosa', kwargs={'kode_pasien': kode_pasien})

        # Redirect ke halaman detail diagnosa
        return redirect(detail_diagnosa_url)

    # Logika jika metode bukan POST, misalnya menampilkan formulir lagi
    return render(request, 'diagnosa.html', {'gejala_list': Gejala.objects.all(), 'keterangan_list': Keterangan.objects.all()})

def detail_diagnosa(request, kode_pasien):
    # Logika untuk menampilkan halaman detail diagnosa berdasarkan kode_pasien
    user_pasien = UserPasien.objects.get(kode_pasien=kode_pasien)
    a_list = ast.literal_eval(user_pasien.p1)
    p1_list = [float(elem) for elem in a_list]
    b_list = ast.literal_eval(user_pasien.p2)
    p2_list = [float(elem) for elem in b_list]
    c_list = ast.literal_eval(user_pasien.p3)
    p3_list = [float(elem) for elem in c_list]
    d_list = ast.literal_eval(user_pasien.cf)
    cf_list = [float(elem) for elem in d_list]
    
    # Filter nilai 0
    filtered_p1, filtered_cf1 = filter_nonzero_values(p1_list, cf_list)
    filtered_p2, filtered_cf2 = filter_nonzero_values(p2_list, cf_list)
    filtered_p3, filtered_cf3 = filter_nonzero_values(p3_list, cf_list)

    print(filtered_cf1)
    combined_cf1 = calculate_combined_cf(filtered_p1, filtered_cf1)
    percentage_cf1 = combined_cf1 * 100
    combined_cf2 = calculate_combined_cf(filtered_p2, filtered_cf2)
    percentage_cf2 = combined_cf2 * 100
    combined_cf3 = calculate_combined_cf(filtered_p3, filtered_cf3)
    percentage_cf3 = combined_cf3 * 100
    if percentage_cf3 > 70 :
        print("Berat")
    elif percentage_cf2 > 95 :
        print("Sedang")
    elif percentage_cf1 > 70 :
        print("Ringan")
    
    return render(request, 'detail_diagnosa.html', {'per3': percentage_cf3,'per2': percentage_cf2,'per1': percentage_cf1,'user':user_pasien})