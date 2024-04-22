from django.forms import ModelForm, CharField, TextInput, Textarea
from .models import Quote, Author



class QuoteForm(ModelForm):
    quote = CharField(min_length=5, max_length=500, required=True, widget=Textarea())

    class Meta:
        model = Quote
        fields = ["quote"]
        exclude = ["tags", "author"]

class AuthorForm(ModelForm):
    fullname = CharField(min_length=5, max_length=50, required=True, widget=Textarea())
    born_date = CharField(min_length=5, max_length=50, required=False, widget=Textarea())
    born_location = CharField(min_length=5, max_length=50, required=False, widget=Textarea())
    description = CharField(min_length=5, max_length=1000, required=False, widget=Textarea())
    class Meta:
        model = Author
        fields = ['fullname', 'born_date', 'born_location', 'description']