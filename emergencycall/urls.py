from django.urls import path
from emergencycall.views import show_hospital, get_hospital, new_hospital, hapus

app_name = 'emergencycall'

urlpatterns = [
    path('show-hospital/', show_hospital, name='show_hospital'),
    path('get-hospital/', get_hospital, name='get_hospital'),
    path('new-hospital/', new_hospital, name="new_hospital"),
    path('hapus/<int:id>', hapus, name='hapus'),
]