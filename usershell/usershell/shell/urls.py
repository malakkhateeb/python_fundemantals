from django.urls import path     
from . import views

urlpatterns = [
    path('', views.shell),
    path('shell', views.addUser),
    path('delete/<int:id>', views.delete, name='delete'),

]