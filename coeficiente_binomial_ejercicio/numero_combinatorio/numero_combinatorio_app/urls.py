from django.urls import path
from . import views

app_name = 'numero_combinatorio'

urlpatterns = [
    path('', views.index, name="index"),
    path('result/', views.result, name="result"),
]
