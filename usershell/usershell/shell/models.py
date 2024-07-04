from django.db import models

class User(models.Model):
    first_name= models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.EmailField(unique=True)
    age=models.IntegerField()

def __str__(self):
        return f"{self.first_name} {self.last_name}"


def create_user(first_name, last_name, email, age):
    User.objects.create(first_name=first_name, last_name=last_name, email=email, age=age)

def get_users():
    return User.objects.all()


def delete_user(id):
    member = User.objects.get(id=id)
    member.delete()