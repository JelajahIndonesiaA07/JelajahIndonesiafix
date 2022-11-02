from django.db import models
from django.contrib.auth.models import User

class tempat_wisata_Item(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    nama_tempat_wisata = models.TextField()
    provinsi_tempat_wisata = models.CharField(max_length = 10)
    deskripsi_tempat_wisata = models.TextField()