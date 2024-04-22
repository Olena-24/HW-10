from django import template
from ..models import Quote

register = template.Library()

def get_author(id):
    author_fullname = Quote.objects.filter(author=id).values('author__fullname').distinct().first()
    return author_fullname['author__fullname']


register.filter('author', get_author)