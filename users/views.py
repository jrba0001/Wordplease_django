from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login as django_login, logout as django_logout
from django.views import View
from django.views.generic import ListView

from users.forms import LoginForm, SignupForm


class LoginView(View):

    def get(self, request):
        """
        Muestra el formulario de login
        :param request: objeto HttpRequest
        :return: objeto HttpResponse con el formulario renderizado
        """
        form = LoginForm()
        context = {'form': form}
        return render(request, 'users/login.html', context)

    def post(self, request):
        """
        Procesa el login de un usuario
        :param request: objeto HttpRequest
        :return: objeto HttpResponse con el formulario renderizado
        """
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            # comprobamos si las credenciales son correctas
            user = authenticate(username=username, password=password)
            if user is None:
                messages.error(request, 'Usuario o contraseña incorrecto')
            else:
                # iniciamos la sesión del usuario (hacemos login del usuario)
                django_login(request, user)
                url = request.GET.get('next', 'home')
                return redirect(url)

        context = {'form': form}
        return render(request, 'users/login.html', context)

class LogoutView(View):

    def get(self, request):
        """
        Hace logout de un usuario y le redirige al login
        :param request: objeto HttpRequest
        :return: objeto HttpResponse de redirección al login
        """
        django_logout(request)
        return redirect('home')


class SignupView(View):
    def get(self, request):
        """
        Muestra formulario de registro
        :param request: objeto HttpRequest
        :return: Objeto HttpResponse con el formulario renderizado
        """
        form = SignupForm()
        context = {'form': form}
        return render(request, 'users/signup.html', context)

    def post(self, request):
        """
               Procesa el login de un usuario
               :param request: objeto HttpRequest
               :return: objeto HttpResponse con el formulario renderizado
               """
        form = SignupForm (request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            # comprobamos si existe el usuario
            if User.objects.filter(username = username).exists():
                messages.error(request, 'Ya existe el usuario')
            else:
                email = form.cleaned_data.get('email')
                first_name = form.cleaned_data.get('first_name')
                last_name = form.cleaned_data.get('last_name')
                user = User.objects.create_user(username = username, first_name=first_name, last_name=last_name,
                                                email = email, password=password )
                messages.success(request,"Usuario Creado")
                django_login(request, user)
                return redirect('home')
        username = form.cleaned_data.get('username')
        if username:
            messages.error(request, "Compruebe los campos obligatorios y formato correo")
        else:
            messages.error(request, "Usuario no puede dejarlo en blanco ni existir")
        context = {'form': form}
        return render(request, 'users/signup.html', context)


class List_users (ListView):

    model = User
    template_name = 'users/list_users.html'
    paginate_by = 5

    def get_queryset(self):
        result = super().get_queryset()
        return result

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'WordPlease Práctica JRBA'
        context['claim'] = 'Listado Usuarios'
        return context