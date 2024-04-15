
from django.urls import path
from . import views

urlpatterns = [
    path('hello', views.hello_view, name="hello_url"),
    path('sobre', views.sobre_view, name="sobre_url"),
    path('goodbye', views.goodbye_view),
    path('hello_name/<str:nome>', views.hello_name_view),
]







