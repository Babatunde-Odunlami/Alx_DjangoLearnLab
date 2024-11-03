from django.contrib import admin
from bookshelf.models import Book

# Configure the list_display, search_fields, and list_filter custom options

class BookAdmin(admin.ModelAdmin):
    #columns to display in the list
    list_display = ("title", "author", "publication_year")
    #fields to search
    search_fields = ("title", "author")
    #fields to filter by
    list_filter = ("publication_year", )

# register the model
admin.site.register(Book, BookAdmin)
