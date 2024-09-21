from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from .views import CustomLoginView, registro
from .views import bienvenido

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registro/', CustomLoginView.as_view(), name='registro'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('bienvenido/', bienvenido, name='bienvenido'),
]
