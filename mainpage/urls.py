from django.urls import path
from mainpage.views import show_mainpage
from mainpage.views import register
from mainpage.views import login_user
from mainpage.views import logout_user


app_name = 'mainpage'


urlpatterns = [
    path('', show_mainpage, name='show_mainpage'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]