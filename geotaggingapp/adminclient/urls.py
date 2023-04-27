from . import views
from django.urls import path


urlpatterns = [
    # path('', views.adminclientview, name='adminclientview'),
    path('', views.qr_gen, name='qr_gen'),
    path('send', views.qr_gen, name='qr_gen'),
    path('',views.index),
]

app_name = "adminclient"