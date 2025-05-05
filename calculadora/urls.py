
from django.urls import path
from . import views 

app_name = 'app_calculadora'

urlpatterns = [
    path('', views.calculadora_view, name="calculadora"),
]

