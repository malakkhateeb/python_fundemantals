from django.shortcuts import render, redirect
from .models import *

def index(request):
    context={
        'dojoos':add_all()
    }
    return render(request, 'index.html', context)


def addDojo(request):
    if request.method=="POST":
        add_Dojo(request)
    return redirect('/')

def addNinja(request):
    if request.method=="POST": 
        add_Ninja(request)
    return redirect('/')

def delDojo(request,id):
    if request.method=="POST":
        remove_dojos(id)
    return redirect('/')

