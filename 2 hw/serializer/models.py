from django.db import models
class Car(models.Model):
    name=models.CharField(max_length=60)
    description=models.TextField(default="Описания нету")
    price=models.DecimalField(max_digits=10,decimal_places=2)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name="Машина"
        verbose_name_plural="Машины"
# Create your models here.
