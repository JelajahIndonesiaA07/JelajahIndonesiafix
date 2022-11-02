from django import forms
from tempat_kuliner.models import tempat_kuliner_Item

class KulinerForm(forms.ModelForm):
    class Meta:
        model = tempat_kuliner_Item
        fields = {"nama_tempat_kuliner", "rating_tempat_kuliner", "lokasi_tempat_kuliner"}