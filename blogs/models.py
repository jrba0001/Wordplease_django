from datetime import timezone

from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class categoria (models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=150, blank=True, null=True)
    def __str__(self):
        """
        Define cómo se representa un Ad como una string
        """
        return '{0} - Author: {1} '.format(self.nombre , self.descripcion)
class blog (models.Model):
    owner = models.OneToOneField(User, related_name="blog",on_delete=models.CASCADE)
    titulo = models.CharField(unique=True, max_length=100)
    descripcion = models.TextField(null=True, blank=True)
    activo = models.BooleanField(default=True)
    imagen = models.ImageField(null=True, blank=True,  upload_to='./')
    publish_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)


    def __str__(self):
        """
        Define cómo se representa un Ad como una string
        """
        return '{0} - Author: {1} '.format(self.titulo , self.owner)


class post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(blog,on_delete=models.CASCADE)
    titulo = models.TextField(unique=True)
    intro = models.TextField(null=True, blank=True)
    cuerpo = models.TextField(null=True, blank=True)
    imagen =  models.ImageField(null=True, blank=True,  upload_to='./')
    categoria= models.ManyToManyField(categoria)
    fpublicacion = models.DateTimeField(null = True, blank=True)
    publish_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    def get_categoria(self):
        return ",".join([str(c.nombre) for c in self.categoria.all()])

    def __str__(self):
        """
        Define cómo se representa un Ad como una string
        """
        return '{0} {1} '.format(self.titulo, self.owner)



