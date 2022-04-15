from django.views import generic
from .models import Servicio


class ServiciosView(generic.ListView):
    model = Servicio
    template_name = "servicios/servicios.html"
