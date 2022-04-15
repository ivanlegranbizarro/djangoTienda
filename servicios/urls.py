from django.urls import path
from . import views

app_name = 'servicios'

urlpatterns = [
    path('', views.ServiciosView.as_view(), name='lista-servicios')
]
