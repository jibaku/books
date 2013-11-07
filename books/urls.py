from books.views import BooksList
from books.views import BookDetail
from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$', BooksList.as_view(), name='books-index'),
    url(r'^(?P<slug>[-\w]+)$', BookDetail.as_view(), name='books-details'),
)