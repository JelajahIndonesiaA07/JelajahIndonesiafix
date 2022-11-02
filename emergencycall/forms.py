from django import forms

from emergencycall.models import EmergencyCallItem

class HospitalForm(forms.ModelForm):
    class Meta:
        model = EmergencyCallItem
        fields = {"hospital_name", "hospital_number", "hospital_location"}
