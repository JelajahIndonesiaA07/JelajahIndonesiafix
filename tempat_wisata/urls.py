from django.urls import path, include

from tempat_wisata.views import allData, index
from rest_framework import routers

urlpatterns = [
    path('', index, name='index'),
    path('all-data/', allData, name="all-data"),
]
