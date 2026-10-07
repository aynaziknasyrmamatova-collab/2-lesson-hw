from django.contrib import admin

# Register your models here.

from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    # Поля, которые будут отображаться в списке в админке
    list_display = ('id', 'title', 'status', 'priority', 'due_date', 'created_at')
    
    # Поля, по которым можно фильтровать задачи в правой колонке
    list_filter = ('status', 'priority', 'due_date')
    
    # Поля, по которым будет работать поиск (по названию и описанию)
    search_fields = ('title', 'description')
    
    # Ограничиваем редактирование системных полей (они будут только для чтения)
    readonly_fields = ('created_at', 'updated_at')
