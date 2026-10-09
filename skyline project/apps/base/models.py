from django.db import models

# Create your models here.
class Settings(models.Model):
    title=models.CharField(max_length=250,verbose_name="Название сайта")
    descriptions=models.TextField(verbose_name='описание')
    logo=models.ImageField(upload_to='logo/')
    phone=models.CharField(max_length=255,verbose_name='Телефонный номер')
    email=models.EmailField(verbose_name='Почта электронная')
    address=models.CharField(max_length=250, verbose_name='Адрес')
    locate_url=models.URLField(verbose_name='Ссылка адреса')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name='Основная настройка'
        verbose_name_plural="Основные настройки"
class Banner(models.Model):
    title=models.CharField(max_length=255,verbose_name='Заголовок')
    subtitle=models.CharField(max_length=255, verbose_name='Подзаголовок')
    description=models.TextField(verbose_name="Описание")
    image=models.ImageField(upload_to='banner_image', verbose_name="Изображение")

    def __str__(self):
            return self.title
    class Meta:
        verbose_name='Баннер'
        verbose_name_plural="Баннеры"
class Numbers(models.Model):
     age=models.IntegerField(verbose_name="Лет в небе")
     destinations=models.IntegerField(verbose_name="направлений")
     people=models.CharField(max_length=275,verbose_name="пассажиров в небе")
     reis=models.IntegerField(verbose_name="Рейсов в небе")
     def __str__(self):
                 return self.title
     class Meta:
             verbose_name='Баннер'
             verbose_name_plural="Баннеры"
class Tour (models.Model):
      image=models.ImageField(upload_to="tour/", verbose_name="Изображение")
      title=models.CharField(max_length=255, verbose_name="Название тура")
      subtitle=models.CharField(max_length=255, verbose_name="Подзаголовок")
      price=models.CharField(max_length=255, verbose_name="Цена")
      class Meta:
                verbose_name='Тур'
                verbose_name_plural="Туры"