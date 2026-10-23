from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="profile",
    )
    phone = models.CharField(max_length=50, verbose_name="Номер телефона")
    balance = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        validators=[MinValueValidator(0)],
        verbose_name="Внутренний баланс",
    )

    class Meta:
        verbose_name = "профиль пользователя"
        verbose_name_plural = "профили пользователей"

    def __str__(self):
        return self.user.get_username()
