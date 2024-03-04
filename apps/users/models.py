from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    age = models.PositiveSmallIntegerField(
        blank=True, null=True
    )
    job = models.CharField(
        max_length=256,
        blank=True, null=True
    )
    gender = models.CharField(
        max_length=50,
        blank=True, null=True
    )
    phone_number = models.CharField(
        max_length=13,
        blank=True, null=True
    )
    instagram = models.URLField(
        blank=True, null=True
    )
    tiktok = models.URLField(
        blank=True, null=True
    )
    apple_id = models.CharField(
        max_length=256
    )
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
    
    def __str__(self) -> str:
        return self.first_name
    