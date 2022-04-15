from django.urls import path
from . import views

app_name = 'autenticacion'

urlpatterns = [
    path('', views.RegistroView.as_view(), name='autenticacion'),
    path('logout/', views.cerrar_sesion, name='logout'),
    path('login/', views.login_user, name='login'),
]
