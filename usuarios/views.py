from django.shortcuts import redirect, render
from .forms import CadastroUsuarioForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm


def cadastro_view(request):

    if request.method == "POST":

        form = CadastroUsuarioForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("login")

    else:

        form = CadastroUsuarioForm()

    return render(
        request,
        "usuarios/cadastro.html",
        {
            "form": form
        }
    )


def login_view(request):

    if request.method == "POST":

        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            usuario = authenticate(
                request,
                username=username,
                password=password,
            )

            if usuario is not None:

                login(request, usuario)

                return redirect("home")

    else:

        form = AuthenticationForm()

    return render(
        request,
        "usuarios/login.html",
        {
            "form": form
        }
    )


def logout_view(request):

    logout(request)

    return redirect("home")