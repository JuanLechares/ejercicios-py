from django.db import models

class Producto(models.Model):
    nombre= models.CharField(max_length="100")
    precio= models.DecimalField()
    envioGratis = models.BooleanField(default=False)
    def __str__(self) -> str:
        return self.title