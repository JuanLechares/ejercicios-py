from django.shortcuts import render
from . models import Producto

def crear_producto(request):
    producto = Producto.objects.create(
        nombre = "Mayonesa Natura",
        descripcion = "La mayonesa es una salsa emulsionada a base de huevo crudo, aceite, sal y algún líquido ácido",
        precio = 9.99
    )
    return render(request, "producto.html", {"producto": producto})
