from django.contrib import admin
from .models import Books
# Register your models here.
@admin.register(Books)
class AdminBooks(admin.ModelAdmin):
    list_display=('id','author', "title",'description', 'price' ,'year', 'image')
    search_fields= ('title', 'author')
