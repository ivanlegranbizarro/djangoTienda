def importe_total_carrito(request):
    total = 0
    if 'carrito' in request.session and request.user.is_authenticated:
        for key, value in request.session['carrito'].items():
            total += float(value['precio'])
    return {'importe_total_carrito': round(total, 2)}
