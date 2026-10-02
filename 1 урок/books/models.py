from django.db import models
class Books(models.Model):
    author=models.CharField(max_length=40,verbose_name="Автор")
    title=models.CharField(max_length=70,verbose_name="Название")
    description=models.TextField(verbose_name="Описание")
    price=models.DecimalField(max_digits=10,decimal_places=2,verbose_name="Цена")
    year=models.DateField(auto_now=True,verbose_name="Год выпуска")
    def __str__(self):
        return self.title
    class Meta:
        verbose_name="Книга"
        verbose_name_plural="Книги"
# Create your models here.
