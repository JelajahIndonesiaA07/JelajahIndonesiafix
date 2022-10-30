from django.urls import path
from .views import index, hasil

app_name = "kuisioner"
urlpatterns = [
    path('', index, name='index'),
    path('hasil', hasil, name='hasil')
]
