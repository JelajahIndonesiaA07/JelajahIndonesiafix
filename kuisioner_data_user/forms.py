from django import forms
from .models import kuisioner


class AssessmentForm(forms.ModelForm):
    class Meta:
        model = kuisioner
        fields = "__all__"
