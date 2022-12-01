from django.urls import path
from emergencycall.views import show_hospital, get_hospital, new_hospital, hapus, show_hospital_json

app_name = 'emergencycall'

urlpatterns = [
    path('show-hospital/', show_hospital, name='show_hospital'),
    path('get-hospital/', get_hospital, name='get_hospital'),
    path('new-hospital/', new_hospital, name="new_hospital"),
    path('hapus/<int:id>', hapus, name='hapus'),
    path('get-hospital-flutter/', show_hospital_json, name="show_hospital_json"),
]