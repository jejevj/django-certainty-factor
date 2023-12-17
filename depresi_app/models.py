from django.db import models


# Kelas Untuk Gejala
class Gejala(models.Model):
    kode_gejala = models.CharField(max_length=3, unique=True)
    keterangan_gejala = models.TextField()
    p1 = models.CharField(max_length=50)
    p2 = models.CharField(max_length=50)
    p3 = models.CharField(max_length=50)

    def __str__(self):
        return self.kode_gejala


# Kelas Untuk User
class UserPasien(models.Model):
    nama = models.CharField(max_length=100)
    jurusan = models.CharField(max_length=100)
    kode_gejala = models.CharField(max_length=100, default="")
    p1 = models.CharField(max_length=100,default="")
    p2 = models.CharField(max_length=100,default="")
    p3 = models.CharField(max_length=100,default="")
    cf = models.CharField(max_length=100,default="")
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.nama


# Kelas Untuk Keterangan
class Keterangan(models.Model):
    kode_keterangan = models.BigAutoField(
        unique=True, primary_key=True, auto_created=True
    )
    keterangan = models.TextField()
    cf = models.CharField(max_length=50)

    def __str__(self):
        return self.kode_keterangan
