from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import *

urlpatterns = [
    path("", DashboardView.as_view(), name="dashboard"),
    path("historical/", HistoricalView.as_view(), name="historical"),
    path("rema/", RemaView.as_view(), name="rema"),
    path("rema/<str:measure>", RemaView.as_view(), name="rema"),
    path('city_data/', get_city_data, name='get_city_data'),
    path('city_info/', get_new_json, name='get_new_json'),
    path("mapJson/", get_map_json, name="mapJson"),
    path("mapJson/<str:measure>", get_map_json, name="mapJson"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("historical/data", download_csv_data, name="historical-data"),
]



