from django.contrib import admin
from .models import Books
@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display=('id','author', 'title', 'description', 'price', 'year')
    list_filter=('author','title')
    search_fields=('author', 'title', 'description')
# Register your models here.
