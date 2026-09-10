from django.db import models

class Employee(models.Model):
    first_name=models.CharField(max_length=50,verbose_name="Имя")
    last_name=models.CharField(max_length=50,verbose_name="Фамилия")
    position=models.CharField(max_length=100,verbose_name="Позиция")
    salary=models.IntegerField(verbose_name="Возраст")
    created_at=models.DateTimeField(auto_now_add=True)

# Create your models here.
