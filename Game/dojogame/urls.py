from django.urls import path     
from . import views

urlpatterns = [
    path('', views.great),
    path('greatnum', views.randNum),
    path('playagain', views.clearData)
]