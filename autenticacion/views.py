from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages


class RegistroView(generic.View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'autenticacion/registro.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home:home')
        else:
            for e in form.errors:
                messages.error(request, form.errors[e])
            return render(request, 'autenticacion/registro.html', {'form': form})


def cerrar_sesion(request):
    logout(request)
    return redirect('home:home')


def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home:home')

        else:
            for e in form.errors:
                messages.error(request, form.errors[e])
            return render(request, 'autenticacion/login.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'autenticacion/login.html', {'form': form})
