from django import forms
from activity.models import Task

class CreateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = {"title","description"}
