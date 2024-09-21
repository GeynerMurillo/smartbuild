from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

# Vista de inicio de sesión personalizada
class CustomLoginView(LoginView):
    template_name = 'mi_app/login.html'

# Vista de la página principal
def home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'mi_app/home.html')
