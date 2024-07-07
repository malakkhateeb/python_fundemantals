from django.db import models

class Dojo(models.Model):
    name= models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state=models.CharField(max_length=2)
    desc = models.TextField(default="old dojo")

    def __str__(self):
        return self.name 

class Ninja(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    dojos=models.ForeignKey(Dojo, related_name="dojon", on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name