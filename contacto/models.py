from django.db import models

# Create your models here.
class FormularioContacto(models.Model):
    nombre= models.CharField(max_length=100)
    email=models.EmailField(null=False, blank=False)
    telefono=models.CharField(max_length=10)
    asunto=models.CharField(max_length=50, blank=True)
    mensaje=models.TextField()
    
    def __str__(self):
        return self.nombre