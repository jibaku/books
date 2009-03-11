from django.db import models
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.contrib.sites.managers import CurrentSiteManager
import datetime

class Author(models.Model):
    user = models.ForeignKey(User)
    birthday = models.DateField(default=datetime.date.today, blank=True)

    def __unicode__(self):
        return self.user.get_full_name() or self.user.username

class Editor(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __unicode__(self):
        return self.name

def cover_filename(instance, filename):
    return "books/%s.jpg" % instance.slug
            
class Book(models.Model):
    site = models.ForeignKey(Site)

    lang = models.CharField(max_length=5)
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, db_index=True)
    authors = models.ManyToManyField(Author)
    editor = models.ForeignKey(Editor)
    isbn_10 = models.CharField(max_length=10, unique=True)
    isbn_13 = models.CharField(max_length=13, unique=True)
    asin = models.CharField(max_length=20, unique=True)
    description = models.TextField()
    cover = models.ImageField(upload_to=cover_filename)
    
    objects = models.Manager()
    on_site = CurrentSiteManager()
    
    def __unicode__(self):
        return self.title
    
    @property
    def affiliate_url(self):
        return "http://www.amazon.fr"

