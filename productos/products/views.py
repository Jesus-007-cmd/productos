
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.shortcuts import render, redirect

from .models import Productos
from .forms import ProductForm

#crear una función simple que me va a retornar el servidor
def index(request):
 
    return HttpResponse("Hola Mundo")




class Insertar(View):
    template_name = "ingresar_productos.html"

    def post(self, request):
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ingresar_productos')
        
        return render (request, self.template_name, {'form': form})
    
    def get(self, request):
        productos=Productos.objects.all()
        form = ProductForm()
        return render (request, self.template_name, {'form': form, 'productos': productos })
    
class Ver(View):
    template_name = "Productos.html"
    def get(self, request):
        productos=Productos.objects.all()
        form = ProductForm()
        return render (request, self.template_name, {'form': form, 'productos': productos })

def insertar_producto(request):
    nuevo_producto = Productos(
        nombre="Monitor",
        descripcion="30 pulgadas 144 hz marca samsung",
        precio=8999,
        fecha_de_registro='2023-07-04',
        estatus=50
    )
    nuevo_producto.save()
    return HttpResponse("Producto insertado correctamente") 