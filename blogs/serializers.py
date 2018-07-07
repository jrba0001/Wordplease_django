from rest_framework import serializers

from blogs.models import blog, post

class blogSerializer(serializers.ModelSerializer):
    class Meta:
        model = blog
        fields = ('owner', 'titulo', 'descripcion', 'activo', 'imagen')

class postSerializer(serializers.ModelSerializer):
    class Meta:
        model = post
        fields = ('titulo','imagen','cuerpo','fpublicacion')


