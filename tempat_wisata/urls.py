from django.urls import path, include

from tempat_wisata.views import allData, index
# from tempat_wisata.viewset_api import *
from rest_framework import routers

urlpatterns = [
    path('', index, name='index'),
    path('all-data/', allData, name="all-data"),
]
