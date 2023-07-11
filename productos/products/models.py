from django.db import models
import datetime
# Create your models here.
class Productos(models.Model):
    nombre = models.CharField("Nombre", max_length=300, default="Sin nombrar")
    descripcion = models.CharField("Descripcion", max_length=300, default="Sin especificar")
    precio = models.IntegerField("Precio",  default=0)
    fecha_de_registro = models.DateField("Fecha de registro",  default=datetime.date.today())
    estatus = models.IntegerField("Estatus",  blank=False)

    def _str_(self):
            return self.nombre