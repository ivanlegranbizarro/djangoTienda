from django.contrib import admin
from .models import Producto, CategoriaProducto


class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categorias', 'precio', 'disponibilidad')
    list_filter = ('categorias',)
    search_fields = ('nombre',)
    readonly_fields = ('creado', 'actualizado')


class CategoriaProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'creado', 'actualizado')
    search_fields = ('nombre',)
    readonly_fields = ('creado', 'actualizado')


admin.site.register(Producto, ProductoAdmin)
admin.site.register(CategoriaProducto, CategoriaProductoAdmin)
