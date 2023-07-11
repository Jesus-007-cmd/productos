from typing import Any, Dict
from django import forms
from .models import Productos

class ProductForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = ['nombre','descripcion', 'precio','fecha_de_registro','estatus']
    #Este metodo clean permitira validar que los campos tengan todos los datos en caso de que nos
    #  mandara mensaje: rellena este campo
    def clean(self):
        cleaned_data = super().clean()
        nombre = cleaned_data.get('nombre') #que empate o tenga los atributos en mi modelo titulo
        descripcion = cleaned_data.get('descripcion')
        precio = cleaned_data.get('precio')
        fecha_de_registro = cleaned_data.get('fecha_de_registro')
        estatus = cleaned_data.get('estatus')

        #validaremos que no tenga valor ninguno de estos campos:
        if not nombre or not descripcion or not precio or not fecha_de_registro or not estatus:
            #se gnera una excpecion directamente con el metodo raise:
             # este genera una exceepcion y retrona un json response al html con el mensaje que se ponga
            raise forms.ValidationError("Todos los campos deben estar completos") #este mensaje se mandara como un log
        return cleaned_data #regrsa el cleaned_data el cual ya se encargo todo el proceso
