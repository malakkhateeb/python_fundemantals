from django.db import models

class Dojo(models.Model):
    name= models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state=models.CharField(max_length=2)
    desc = models.TextField(default="old dojo")

    def __str__(self):
        return f"{self.name}" 

class Ninja(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    dojos=models.ForeignKey(Dojo, related_name="dojon", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"    
    
def add_all():
    return Dojo.objects.all()

def add_Dojo(M):
    name=M.POST['Name']
    city=M.POST['city']
    state=M.POST['state']
    return Dojo.objects.create(
            name=name,
            city=city,
            state=state)

def F_key(id):
    return Dojo.objects.get(id=id)


def add_Ninja(request):
    Ninja.objects.create(
    first_name=request.POST['FirstName'],
    last_name=request.POST['LastName'],
    dojos=F_key(request.POST['id']))       
    

def remove_dojos(id):
    remove=Dojo.objects.get(id=id)
    remove.delete()

