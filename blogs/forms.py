import datetime

from django.forms import ModelForm
from django import forms


from blogs.models import blog, post


class nuevo_form (ModelForm):

    class Meta:
        model = blog
        fields = ['titulo','descripcion','imagen']
        labels = {
            'titulo':'Título del Blog',
            'descripcion':'Descripción del Blog',
            'imagen': 'Imagen'}

        exclude=['owner','activo']

class new_post (ModelForm):

    class Meta:
        model = post
        fields = ['owner','blog','titulo','intro','cuerpo','imagen','categoria','fpublicacion']
        labels = {
            'blog':'Blog',
            'titulo':'Titulo del Post',
            'intro': 'Introducción',
            'cuerpo': 'Cuerpo del Post',
            'imagen':'Imagen destacada',
            'Categoría':'Categorías',
            'fpublicacion' : 'Fecha de Publicación',
        }
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'intro': forms.TextInput(attrs={'class': 'form-control'}),
            'cuerpo': forms.TextInput(attrs={'class': 'form-control'}),
            'fpublicacion': forms.SelectDateWidget(attrs={'class': 'DateTimeInput'}),

        }
        exclude=['owner']
