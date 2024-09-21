from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Página principal, accesible solo para usuarios autenticados
    path('login/', views.CustomLoginView.as_view(), name='login'),  # Página de inicio de sesión
]