from django import forms
from tempat_wisata.models import tempat_wisata_Item

class WisataForm(forms.ModelForm):
    class Meta:
        model = tempat_wisata_Item
        fields = {"nama_tempat_wisata", "provinsi_tempat_wisata", "deskripsi_tempat_wisata"}
