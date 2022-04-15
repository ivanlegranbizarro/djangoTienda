from django.urls import path
from . import views

app_name = 'tienda'

urlpatterns = [
    path('', views.ProductoView.as_view(), name='lista-productos')
]
