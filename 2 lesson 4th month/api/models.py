from django.db import models

# Create your models here.
class Books(models.Model):
    author = models.CharField(max_length=120,verbose_name='Автор книги')
    title = models.CharField(max_length=60,verbose_name="Название книги")
    description = models.TextField(blank=True, verbose_name="Описание книги", default="Без описания")
    price = models.DecimalField(max_digits=10, decimal_places=2,verbose_name="Цена книги")
    year = models.DateField(null=True, blank =True)
    image=models.ImageField(upload_to='book_image/',null=True, blank=True, verbose_name="Изображение книги")
    def __str__(self):
        return self.author
    class Meta:
        verbose_name= "Книга"
        verbose_name_plural= "Книги"

