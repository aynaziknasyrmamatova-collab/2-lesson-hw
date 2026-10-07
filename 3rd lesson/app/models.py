from django.db import models
from decimal import Decimal
from django.core.validators import MaxValueValidator,MinValueValidator
# Create your models here.
class Task(models.Model):
    class StatusChoices(models.TextChoices):
        PENDING='pending','Ожидает'
        IN_PROGRESS='in_progress','В процессе'
        COMPLETED='completed','Завершено'
    title=models.CharField(max_length=150,verbose_name="Описание задачи")
    description=models.TextField(blank=True,null=True,verbose_name="Подробное описание")
    status=models.CharField(
        max_length=20,
        choices=StatusChoices.choices,
        default=StatusChoices.PENDING,
        verbose_name="Статус"
    )
    priority=models.IntegerField(default=3,validators=[MinValueValidator(1),MaxValueValidator(5)], verbose_name="Приоритет")
    due_date=models.DateTimeField(
        blank=True,
        null=True,
        verbose_name="Дедлайн"
    )
    created_at=models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )
    updated_at=models.DateTimeField(
        auto_now=True,
        verbose_name="Дата обновления"
    )
    def __str__(self):
        return self.title
    class Meta:
        verbose_name="Задача"
        verbose_name_plural="Задачи"
    