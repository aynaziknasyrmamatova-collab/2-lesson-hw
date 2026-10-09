from django.db import models
from decimal import Decimal
from django.core.validators import MinValueValidator, MaxValueValidator

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Категория", unique=True)
    description = models.TextField(blank=True, verbose_name='Описание категории')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name', ]

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='products',
        verbose_name='Категория',
        blank=True,
        null=True,
    )
    price = models.DecimalField( 
        'Цена',
        max_digits=10,
        decimal_places=2, 
        validators=[MinValueValidator(Decimal('0.01'))]
    )
    discount = models.PositiveSmallIntegerField(
        'Скидка в процентах',
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(70)] 
    )
    title = models.CharField(max_length=100, verbose_name="Название товара")
    description = models.TextField(blank=True, verbose_name='Описание товара')
    
    stock = models.PositiveIntegerField('Остаток товара', default=0)
    is_in_sale = models.BooleanField('На продаже', default=True)

    created_at = models.DateTimeField("Дата создания", auto_now_add=True)
    update_et = models.DateTimeField("Дата Обновления", auto_now=True)

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        ordering = ['title']
    
    def __str__(self):
        return f"{self.title} (Цена: {self.price})"

    