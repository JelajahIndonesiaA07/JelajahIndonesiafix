from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.


class kuisioner(models.Model):
    nama = models.CharField(max_length=255)
    umur = models.IntegerField()
    gender = models.CharField(max_length=10)
    vaksin = models.CharField(max_length=10)
    negara = models.CharField(max_length=255)
    tujuan = models.CharField(max_length=255)
    prov = models.CharField(max_length=255)
    kontak = models.CharField(max_length=15)

    def __str__(self):
        return str(self.nama)
