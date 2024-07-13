from django.urls import path     
from . import views

urlpatterns = [
    path('', views.indexBooks),
    path('books', views.addBooks),
    path('showbooks/<int:id_book>',views.showBooks),
    path('selectauthors/<int:id_book>',views.selectauthors),
    path('authorsinfo',views.indexAuthors),
    path('authors',views.addAuthors ),
    path('showauthors/<int:id_author>',views.showAuthors),
    path('selectbooks/<int:id_author>',views.selectBooks)
    
]