from django.db import models
class Settings(models.Model):
    title=models.CharField(max_length=255, verbose_name="Название компании")
    description=models.TextField(verbose_name="Описание")
    logo=models.ImageField(upload_to="logo/",verbose_name="Логотип")
    phone=models.CharField(max_length=255, verbose_name="Номер телефона")
    email=models.EmailField(verbose_name="Email")
    address=models.CharField(max_length=255,verbose_name="Адрес")
    social_media_url=models.URLField(verbose_name="Ссылка на соцсети")
    years_on_market=models.CharField(max_length=50,default="15+",verbose_name="Лет на рынке")
    cars_in_stock=models.CharField(max_length=50,default="200+",verbose_name="Автомобилей в наличии")
    happy_clients=models.CharField(max_length=50,default="4 800",verbose_name="Довольных клиентов")
    def __str__(self):
        return self.title
    class Meta: 
        verbose_name="Основная настройка"
        verbose_name_plural="Основные настройки"
class Service(models.Model):
    title=models.CharField(max_length=255, verbose_name="Название услуги")
    description=models.TextField(verbose_name="Описание")
    price=models.CharField(max_length=255,verbose_name="Цена")
    image=models.ImageField(upload_to="image/",verbose_name="Изображение")
    def __str__(self):
        return self.title
    class Meta: 
        verbose_name="Модель для услуг"
        verbose_name_plural="Модели для услуг"


class Slide(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to="slides/", verbose_name="Изображение")
    button_text = models.CharField(max_length=100, default="Смотреть каталог", verbose_name="Текст кнопки")
    button_url = models.CharField(max_length=255, default="/catalog/", verbose_name="Ссылка кнопки")
    order = models.PositiveIntegerField(default=0, verbose_name="Порядок")
    is_active = models.BooleanField(default=True, verbose_name="Показывать")

    class Meta:
        ordering = ["order", "id"]
        verbose_name = "Слайд"
        verbose_name_plural = "Слайды"

    def __str__(self):
        return self.title
        