from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    class Meta:
        verbose_name="Книга"
        verbose_name_plural="Книги"
    def __str__(self):
        return self.title
class Check(models.Model):
    title=models.CharField(max_length=100,verbose_name="Название банка")
    author=models.CharField(max_length=50,verbose_name="Имя пользователя")
    number=models.IntegerField(verbose_name="номер счет")
    money=models.IntegerField(verbose_name="Количество денег на балансе")

    class Meta:
        verbose_name="Главная характеристика"
        verbose_name_plural="Главные характеристики"
    def __Str__(self):
        return self.title
