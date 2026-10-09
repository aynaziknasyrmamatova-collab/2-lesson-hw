from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    age = models.IntegerField(verbose_name="Возраст")
    city = models.CharField(max_length=100, verbose_name="Город")

    def __str__(self):
        return self.name
