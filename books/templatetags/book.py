import re

from django import template
from django.core.cache import cache
from django.core.urlresolvers import reverse

register = template.Library()

from books.models import Book

class RandomBooksNode(template.Node):
    def __init__(self, var_name):
        self.var_name = var_name

    def render(self, context):
        context[self.var_name] = Book.objects.all().order_by('?')[:5]
        return ''


@register.tag(name="random_books")
def random_books(parser, token):
    """
    {% random_books as books %}
    """
    tokens = token.split_contents()
    if len(tokens) is not 3 and token[0] == 'random_books' and token[0] == 'as':
        raise template.TemplateSyntaxError, "%r tag must be used with %s" % (tokens[0], "{% profile_url user as profil_details %}")
    var_name = tokens[2]
    return RandomBooksNode(var_name)
