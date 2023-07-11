from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ingresar_productos/', views.Insertar.as_view(), name='ingresar_productos' ),
    path('productos/', views.Ver.as_view(), name='productos' ),
    path('index/', views.index, name='index')
    
]
