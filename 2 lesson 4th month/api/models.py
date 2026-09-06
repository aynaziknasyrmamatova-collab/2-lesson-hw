from django.db import models

# Create your models here.
    
class Movies(models.Model):
    author=models.CharField(max_length=120, verbose_name="Режиссер фильма")
    name=models.CharField(max_length=60,verbose_name="Название фильма")
    actors=models.CharField(max_length=60,verbose_name="Главный герой фильма")
    description=models.TextField(blank=True, verbose_name="Описание фильма",default="Без описания")
    year=models.DateField(null=True,blank=True)
    company=models.CharField(max_length=120,verbose_name="Комания фильма")
    def __str__(self):
        return self.author
    class Meta:
        verbose_name="Фильм"
        verbose_name_plural="Фильмы"