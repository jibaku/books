from django.db import models
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.contrib.sites.managers import CurrentSiteManager
import datetime

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
    authors = models.CharField(max_length=200)
    editor = models.ForeignKey(Editor)
    url = models.URLField(blank=True)
    affiliate_url = models.URLField(blank=True)
    isbn_10 = models.CharField(max_length=10, unique=True, null=True, blank=True)
    isbn_13 = models.CharField(max_length=13, unique=True, null=True, blank=True)
    asin = models.CharField(max_length=20, unique=True, null=True, blank=True)
    description = models.TextField()
    cover = models.ImageField(upload_to=cover_filename, blank=True)
    
    objects = models.Manager()
    on_site = CurrentSiteManager()
    
    def __unicode__(self):
        return self.title
