from django.views.generic.list_detail import object_list
from django.views.generic.list_detail import object_detail
from books.models import Book

def books_list(request, page = 1):
    books = Book.on_site.published()
    return object_list(request, queryset=books, allow_empty=False)
    
def book_detail(request, slug):
    books = Book.on_site.published()
    return object_detail(request, queryset=books, slug=slug)
    