from . import views
from django.urls import path


urlpatterns = [
    path('', views.adminclientview, name='adminclientview')
]

app_name = "adminclient"