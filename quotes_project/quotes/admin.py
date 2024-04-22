from django.contrib import admin
from .models import Author, Quote, Tag


# Register your models here.
admin.site.site_header = 'quoter storage'
admin.site.site_title = 'quoter manage'
admin.site.index_title = 'admin panel'


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    class Meta:
        model = Author

    list_display = ('id', 'fullname', 'born_date', 'created_at')
    search_fields = ('fullname',)
    ordering = ('id',)  

@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    class Meta:
        model = Quote

    filter_horizontal = ('tags',)
    list_display = ('id', 'author', 'quote', 'created_at', 'get_tags')
    search_fields = ('author',)
    ordering = ('id',)

    def get_tags(self, object):
        return ', '.join([t.name for t in object.tags.all()])


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    class Meta:
        model = Tag

    list_display = ('id', 'name')
    search_fields = ('name',)
    ordering = ('id',)



