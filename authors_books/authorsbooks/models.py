from django.db import models
#data of authors
class Author(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    notes=models.TextField()
    
    def __str__(self):
        return f"{self.name}"
#data for books
class Book(models.Model):
    title=models.CharField(max_length=255)
    desc=models.TextField()
    authors =models.ManyToManyField(Author, related_name="books")

    def __str__(self):
        return f"{self.title}"

#this method select all the books
def add_all():
    return Book.objects.all()

#this methode to add books after post them 
def add_books(request):
    title=request.POST['title']
    desc=request.POST['description']
    return Book.objects.create(
            title=title,
            desc=desc
    )
#to show the results after add books 
def show_book(id):
    return Book.objects.get(id=id)

#this method to  select all the authors
def add_all_authors():
    return Author.objects.all()

#this method to add new authors 
def add_authors(request):
    first_name=request.POST['first_name']
    last_name=request.POST['last_name']
    notes=request.POST['notes']
    return Author.objects.create(
            first_name=first_name,
            last_name=last_name,
            notes=notes
    )
#this method to show the results after selection 
def show_authors(id):
    return Author.objects.get(id=id)


