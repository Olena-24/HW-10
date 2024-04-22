import os
import django

from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker
from .models_sql import session, Author as Author_1, Quote as Quote_1, Tag as Tag_1, QuoteTag


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quotes_project.settings')
django.setup()

from quotes.models import Author, Quote, Tag


authors = session.query(Author_1).all()


for author in authors:
    Author.objects.get_or_create(
        fullname = author.fullname[:50],
        born_date = author.born_date[:50],
        born_location = author.born_location[:50],
        description =author.description
    )

quotes = session.query(Quote_1).all()

for quote in quotes:
    tags = []
    q_tags = session.query(Tag_1.name).select_from(QuoteTag).join(Tag_1).join(Quote_1).filter(quote.id==QuoteTag.quote_id).group_by(Tag_1.name).all()
   
    for tag in q_tags:
        t, *_ = Tag.objects.get_or_create(name=tag[0])
        tags.append(t)

    exist_quote =  bool(len(Quote.objects.filter(quote=quote.quote)))

    if not exist_quote:
        author = session.query(Author_1).filter(Author_1.id==quote.author_id).first()
        a = Author.objects.get(fullname=author.fullname)
        q = Quote.objects.create(
            quote=quote.quote,
            author=a
        )
        for tag in tags:
            q.tags.add(tag)


    
