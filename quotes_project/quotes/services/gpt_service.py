import random
import re
from django.conf import settings
from openai import OpenAI


from ..models import Author, Quote, Tag


client = OpenAI(api_key=settings.OPEN_AI_KEY)


def ask_gpt(prompt, author):

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": f"Image you are a {author}"},
            {"role": "user", "content": prompt}
        ]
    )

    return completion.choices[0].message.content

def generate_random_quote():
    authors = Author.objects.all()
    author = random.choice(authors)
    prompt = f'Come up with a quote by author is {author.fullname}. Quote must be in English.'
    quote_text_draft = ask_gpt(prompt=prompt, author=author.fullname)
    pattern = r"(?<=\")(.*?)(?=\")"
    quote_match = re.search(pattern, quote_text_draft)
    if quote_match:
        quote_text = quote_match.group()
    else:
        quote_text = quote_text_draft
    quote_tags = quote_text.split(' ')
    tags = []
    for tag in quote_tags:
        if tag.isalpha() and len(tag)>4:
            tags.append(tag)
    tag, *_ = Tag.objects.get_or_create(
        name = random.choice(tags)
    )
    quote = Quote.objects.create(
        quote=quote_text,
        author=author
        )
    quote.tags.add(tag)
    print('Quote was created sucsefuly')


