from django import forms
from activity.models import Task

class CreateForm(forms.Form):
    title = forms.CharField(label = "Title")
    description = forms.CharField(label = "Description")