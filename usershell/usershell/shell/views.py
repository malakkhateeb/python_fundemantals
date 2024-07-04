from django.shortcuts import render, redirect
from .models import *


def shell(request):
    context = {
        'malak': get_users(),
    }
    return render(request, 'shell.html', context)

def addUser(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        age = request.POST['age']
        create_user(first_name, last_name, email, age)
    return redirect('/')

def delete(request,id):
    delete_user(id)
    return render(request, 'shell.html')