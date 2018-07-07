from django.contrib import admin

# Register your models here.
from django.utils.safestring import mark_safe

from blogs.forms import new_post
from blogs.models import categoria, post, blog

admin.site.register(categoria)


admin.site.site_header = 'Django Wordplease Práctica'
admin.site.site_title = 'Django Wordplease Admin'
admin.site.index_title = 'Django Wordplease Admin'

@admin.register(blog)
class blogAdmin(admin.ModelAdmin):
    list_display = ('owner', 'titulo', 'descripcion', 'activo', 'imagen','publish_on','modified_on')

    def user_full_name(self, movie):
        return "{0} {1}".format(blog.user.first_name, blog.user.last_name)

    readonly_fields = ('publish_on', 'modified_on')

    fieldsets = (
        (None, {
            'fields': ('titulo', 'descripcion')
        }),
        ("Imagen", {
            'fields': ('imagen','activo')
        }),
        ("Información adicional", {
            'fields': ('publish_on', 'modified_on')
        }))

class categoriainline(admin.TabularInline):
    model = post.categoria.through


@admin.register(post)
class postAdmin(admin.ModelAdmin):

    readonly_fields = ('publish_on', 'modified_on', 'imagen_html')
    list_display = ('owner', 'blog', 'titulo', 'intro', 'cuerpo', 'imagen','imagen_html','get_categoria','fpublicacion','publish_on','modified_on')
    list_filter = ['owner', 'blog','fpublicacion','categoria']
    search_fields = ['owner__first_name', 'owner__last_name', 'owner__username','blog__titulo']


    def user_full_name(self, post):
        return "{0} {1}".format(post.user.first_name, post.user.last_name)

    def imagen_html(self, post):
        if post.imagen:
            return mark_safe('<img src="{0}" alt="{1}" title="{2}" width="100">'.format(post.imagen.url, post.titulo, post.titulo))
        else:
            return

    fieldsets = (
        (None, {
            'fields': ('owner','titulo', 'intro','cuerpo')
        }),
        ("Imagen", {
            'fields': ('imagen_html','imagen')
        }),
        ("Información adicional", {
            'fields': ('fpublicacion','publish_on', 'modified_on')
        }))
    inlines = [
        categoriainline,
    ]



