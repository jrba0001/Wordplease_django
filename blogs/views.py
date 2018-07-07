from django.utils.datetime_safe import datetime
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, FormView
from django.views.generic.base import View

from blogs.forms import nuevo_form, new_post
from blogs.models import post, blog


class HomeView(ListView):

    model = post
    template_name = 'blog/list.html'
    paginate_by = 5

    def get_queryset(self):
        return super(HomeView, self).get_queryset().filter(fpublicacion__lte=datetime.now()).order_by('-publish_on')[:5]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'WordPlease Práctica JRBA'
        context['claim'] = 'Listado últimos posts publicados por usuarios'
        return context

class List_blogs(ListView):

    model = blog
    template_name = 'blog/list_blogs.html'
    paginate_by = 5

    def get_queryset(self):
        result = super().get_queryset()
        return result

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'WordPlease Práctica JRBA'
        context['claim'] = 'Listado blogs de usuarios'
        return context

class newpost(FormView):
    template_name = "blog/new_post.html"
    form_class = new_post
    success_url = 'home'

    def get(self, request):
        """
        Muestra formulario de registro
        :param request: objeto HttpRequest
        :return: Objeto HttpResponse con el formulario renderizado
        """
        form = new_post
        form.fpublicacion = timezone.now()
        context = {'form': form}
        return render(request, 'blog/new_post.html', context)

    def post(self, request):
        """

        :param request:request
        :return:
        """
        form = new_post (request.POST or None, request.FILES)
        form.fpublicacion =timezone.now()
        usuario = request.user.id

        if form.is_valid():
            instancia = form.save(commit=False)
            instancia.owner = get_object_or_404(User,Q(id=self.request.user.id))
            instancia.save()
            messages.success(request, 'Post creado correctamente')
            return redirect('home')
        else:
            messages.error(request, 'Revise los campos')
            context = {'form': form}
            return render(request, 'blog/new_post.html', context)

        return redirect('home')


class nuevo (FormView):
    template_name = "blog/nuevo_blog.html"
    form_class = nuevo_form
    success_url = 'home'


    def get(self, request):
        """
        Muestra formulario de registro
        :param request: objeto HttpRequest
        :return: Objeto HttpResponse con el formulario renderizado
        """
        form = nuevo_form
        context = {'form': form}
        return render(request, 'blog/nuevo_blog.html', context)

    def post(self, request):
        """
               Procesa el login de un usuario
               :param request: objeto HttpRequest
               :return: objeto HttpResponse con el formulario renderizado
               """
        form = nuevo_form (request.POST or None, request.FILES)
        usuario = request.user.id
        try:
            nuevo = get_object_or_404 (blog, Q(owner=usuario))
        except:
            if form.is_valid():
                instancia = form.save(commit=False)
                instancia.owner = get_object_or_404(User,Q(id=self.request.user.id))
                instancia.activo = True
                instancia.save()
                messages.success(request, 'Blog creado correctamente')
                return redirect('list_blog')

            messages.error(request, 'Revise los campos')
            context = {'form': form}
            return render(request, 'blog/nuevo_blog.html', context)

        messages.error(request, 'EL USUARIO TIENE UN BLOG CREADO')
        return redirect('list_blog')

class blog_personal(ListView):
    model = post
    template_name = 'blog/list_post.html'


    def get_queryset(self):
        result = super().get_queryset()
        usuario = self.kwargs.get('username')
        user = get_object_or_404(User, Q(username=usuario))
        return result.filter(owner=user.id).order_by('-publish_on')[:5]


class post_detail(View):

    def get (self, request, pk):
        try:
            postdet = post.objects.select_related().get(pk=pk)
        except postdet.DoesNotExist:
            # si no existe el post, devolvemos un 404
            messages.error(request, 'No existe el anuncio que buscar, status 404')
            return HttpResponse('No existe el anuncio que buscas', status=404)

        context ={'post':postdet}
        context['title'] = 'WordPlease Práctica JRBA'
        context['claim'] = 'Detalle post {0}'.format(pk)

        # devolver la respuesta utilizando una plantilla
        return render(request, 'blog/detalle.html', context)
