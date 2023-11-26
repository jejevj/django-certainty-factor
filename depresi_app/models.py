from django.db import models


class Gejala(models.Model):
    kode_gejala = models.CharField(max_length=3, unique=True)
    keterangan_gejala = models.TextField()
    p1 = models.CharField(max_length=50)
    p2 = models.CharField(max_length=50)
    p3 = models.CharField(max_length=50)

    def __str__(self):
        return self.kode_gejala
