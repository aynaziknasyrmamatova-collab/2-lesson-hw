from django.db import models
class Product(models.Model):
    title=models.CharField(max_length=200,verbose_name="название товара")
    description=models.TextField(blank=True,verbose_name="описание товара")
    price=models.DecimalField(max_digits=10,decimal_places=2,verbose_name="цена")
    quantity=models.PositiveIntegerField(default=0,verbose_name="количество на складе")
    is_available=models.BooleanField(default=True,verbose_name="в наличии ли товар")
    created_at=models.DateTimeField(auto_now_add=True,verbose_name="дата добавления")
# Create your models here.
