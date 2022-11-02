from .models import filter
from django import forms

class WisataForm(forms.ModelForm):
    class Meta:
        model = filter
        fields = "__all__"
