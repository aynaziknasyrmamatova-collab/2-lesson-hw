from django.db import models
class Task(models.Model):
    title=models.CharField(max_length=60)
    description=models.TextField(default="Описания нету")
    is_complete=models.BooleanField(default=False)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name="Задача"
        verbose_name_plural="Задачи"
# Create your models here.
