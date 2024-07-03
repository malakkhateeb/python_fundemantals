from django.shortcuts import render, redirect
from .models import User

def shell(request):
    context={
        'malak': User.objects.all()
    }
    return render(request,'shell.html',context)

def addUser(request):
    if request.method=='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        age = request.POST['age']

    User.objects.create(first_name=first_name,last_name=last_name,email=email,age=age)
    return redirect('/')