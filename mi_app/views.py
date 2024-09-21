from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.http import HttpResponse

# Vista de inicio de sesión personalizada
class CustomLoginView(LoginView):
    template_name = 'mi_app/login.html'

# Vista de la página principal
def registro(request):
    if not request.user.is_authenticated:
        return redirect('bienvenido')
    return render(request, 'mi_app/home.html')

# Vista de bienvenido
def bienvenido(request):
    print("Accediendo a la vista de bienvenido")
    return HttpResponse("Bienvenido crack :)")