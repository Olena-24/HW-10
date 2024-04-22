from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.db.models import Count

from .models import Quote, Tag, Author
from .forms import QuoteForm, AuthorForm


# Create your views here.
def main(request, page=1):
    quotes = Quote.objects.all()
    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    quotes_on_page = paginator.page(page)
    top_tags = Tag.objects.annotate(quote_count=Count('quote')).order_by('-quote_count')

    return render(request, 'quotes/index.html', context={'quotes': quotes_on_page, 'paginator': paginator, 'top_tags': top_tags})

def about_author(request, quote_id):
    quote = Quote.objects.get(pk=quote_id)
    author = get_object_or_404(Author, id=quote.author.id)
    return render(request, 'quotes/author_about.html', context={'author': author})

def select_by_tag(request, tag_id):
    tag = Tag.objects.get(pk=tag_id)
    quotes = Quote.objects.filter(tags__id=tag_id).all()
    return render(request, 'quotes/select_by_tag.html', context={'tag': tag, 'quotes': quotes})

def select_by_author(request):
    if request.method == 'POST':
        author_request = request.POST.get('author')
        author = get_object_or_404(Author, id=author_request)
        return redirect('quotes:quotes_by_author', author.id)
    authors = Author.objects.all()
    return render(request, 'quotes/select_by_author.html', context={'authors': authors})

def quotes_by_author(request, author_id):
    author = Author.objects.get(pk=author_id)
    quotes = Quote.objects.filter(author=author.id).all()
    return render(request, 'quotes/quotes_by_author.html', context={'quotes': quotes, 'author': author})

@login_required
def add_quote(request):
    if request.method == 'POST':
        quote_text = request.POST.get('quote_text')
        author_id = request.POST.get('author')
        tag_ids = request.POST.getlist('tags')

        author = get_object_or_404(Author, id=author_id)

        quote = Quote.objects.create(
            quote=quote_text,
            author=author,
        )

        tags = Tag.objects.filter(id__in=tag_ids)
        quote.tags.set(tags)

        return redirect('quotes:root')

    authors = Author.objects.all()
    tags = Tag.objects.all()
    return render(request, 'quotes/add_quote.html', context={'authors': authors, "tags": tags})

@login_required
def add_author(request):
    if request.method == 'POST':
        author_fullname = request.POST.get('author_fullname')
        author_born_date = request.POST.get('author_born_date')
        author_born_location = request.POST.get('author_born_location')
        author_description = request.POST.get('author_description')

        author = Author.objects.create(
                fullname = author_fullname,
                born_date = author_born_date,
                born_location = author_born_location,
                description = author_description
            )
        return redirect('quotes:root')
    return render(request, 'quotes/add_author.html')
