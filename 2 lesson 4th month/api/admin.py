from django.contrib import admin
from .models import Movies
# Register your models here.
@admin.register(Movies)
class AdminMovies(admin.ModelAdmin):
    list_display=("id",'author','name','description','year','company')
    search_fields=('name','author')