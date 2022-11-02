from django.urls import path
from activity.views import ShowActivity
from activity.views import ShowActivityForms
from activity.views import AddActivity
from activity.views import show_json

app_name = 'todolist'

urlpatterns = [
    path('', ShowActivity, name='ShowActivity'),
    path("forms/", ShowActivityForms, name='ShowActivityForms'),
    path("submit/", AddActivity, name="AddActivity"),
    path("json/", show_json, name="show_json"),
]