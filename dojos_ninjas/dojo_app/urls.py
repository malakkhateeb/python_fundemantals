from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('dojo',views.addDojo),
    path('ninja',views.addNinja),
    path('remove/<int:id>',views.delDojo)
]