from django.db import models

# Create your models here.
class wisata(models.Model):
    nama = models.CharField(max_length=30)
    provinsi = models.CharField(max_length=30)
    alamat = models.CharField(max_length=200)
    deskripsi = models.CharField(max_length=200)

class filter(models.Model):
    prov= models.CharField(max_length=30)
