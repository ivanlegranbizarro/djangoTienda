from django.views import generic
from .models import Producto, CategoriaProducto


class ProductoView(generic.ListView):
    model = Producto
    template_name = 'tienda/tienda.html'
