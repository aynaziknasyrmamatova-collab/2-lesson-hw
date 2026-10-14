from django.db import models

class AbstractBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
class Zone(AbstractBaseModel):
    name = models.CharField(max_length=100, verbose_name="Название локации")
    location = models.CharField(max_length=100, verbose_name="Город/район")
    coordinates = models.CharField(max_length=100, verbose_name="Координаты")
    description = models.TextField(verbose_name="Описание")

    class Meta:
        ordering = ["name", "id"]
    def __str__(self):
        return self.name
class Visitors(AbstractBaseModel):
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE, related_name="visitors")
    full_name = models.CharField(max_length=200, verbose_name="ФИО")
    info = models.TextField(verbose_name="Информация о посетителе")
    is_allowed = models.BooleanField(verbose_name="Разрешен ли вход")
    class Meta:
        ordering = ["full_name", "id"]

    def __str__(self):
        return self.full_name
