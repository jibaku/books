from django.conf.urls.defaults import *

urlpatterns = patterns('books.views',
    url(r'^$', 'books_list', name='books-index'),
    url(r'^(?P<slug>[-\w]+)$', 'book_detail', name='books-details'),
)