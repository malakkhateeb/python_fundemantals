from django.shortcuts import render, redirect
from .models import *

def indexBooks(request):
    context={
        'books': add_all(),
    }
    return render(request,'books.html', context)

# this method to insirt new books with title and description 
def addBooks(request):
    if request.method== 'POST':
        add_books(request)
        return redirect('/')

#this method to show the results when add new book
def showBooks(request,id_book):
    context={
        'book':show_book(id_book),
        'authors':  Author.objects.exclude(books=id_book)
    }
    return render (request, 'showbooks.html', context)

#this method the main page to add the authors 
def indexAuthors(request):
    context={
        'authors': add_all_authors()
    }
    return render(request, 'authors.html', context)

#this methode to add new authors 
def addAuthors(request):
    if request.method== 'POST':
        add_authors(request)
        return redirect('/authorsinfo')

#this method to show the authors after add them 
def showAuthors(request,id_author):
    context={
        'author':show_authors(id_author),
        'books': Book.objects.exclude(authors=id_author)
    }
    return render (request, 'showauthors.html', context)

#this method to select the authors for each book and execlude the books choosen 
def selectBooks(request,id_author):
    if request.method=='POST':
        this_author= show_authors(id_author)
        book=show_book(request.POST['thisbook'])
        this_author.books.add(book)
    return redirect (f'/showauthors/{id_author}')

#this method to select the books for each authors and execlude the authors choosen
def selectauthors(request,id_book):
    if request.method=='POST':
        this_book= show_book(id_book)
        author=show_authors(request.POST['thisauthor'])
        this_book.authors.add(author)
    return redirect (f'/showbooks/{id_book}')
        
