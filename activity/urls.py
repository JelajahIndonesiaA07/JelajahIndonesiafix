from django.urls import path
from activity.views import ShowActivity
from activity.views import ShowActivityBali
from activity.views import ShowActivityJogja
from activity.views import ShowActivityJabar
# from activity.views import ShowActivityJateng
# from activity.views import ShowActivityJatim
from activity.views import ShowActivityForms
from activity.views import AddActivity
from activity.views import show_json

app_name = 'activity'

urlpatterns = [
    path('', ShowActivity, name="ShowActivity"),
    path('bali/', ShowActivityBali, name="ShowActivityBali"),
    path('jogja/', ShowActivityJogja, name="ShowActivityJogja"),
    path('jabar/', ShowActivityJabar, name="ShowActivityJabar"),
    # path('jateng/', ShowActivityJateng, name="ShowActivityJateng"),
    # path('jatim/', ShowActivityJatim, name="ShowActivityJatim"),
    path("forms/", ShowActivityForms, name="ShowActivityForms"),
    path("submit/", AddActivity, name="AddActivity"),
    path("json/", show_json, name="show_json"),
]