from django.shortcuts import redirect
from .carrito import Carrito
from tienda.models import Producto


def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect('tienda:lista-productos')


def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect('tienda:lista-productos')


def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar_producto(producto)
    return redirect('tienda:lista-productos')


def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.vaciar_carrito()
    return redirect('tienda:lista-productos')
