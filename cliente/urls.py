from . import views
from django.urls import path

urlpatterns = [
    path('buscar/', views.buscar, name='buscar'),
    path('produto/', views.buscar, name='produto'),
]