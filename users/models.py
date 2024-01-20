from random import choice

from django.db import models
from django.contrib.auth.models import AbstractUser

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from rest_framework.authtoken.models import Token

from .managers import UserManager


class User(AbstractUser):
    username = None
    email = models.EmailField(
        verbose_name="Элетронная почта",
        max_length=255,
        unique=True,
    )
    first_name = models.CharField("Имя", max_length=255, blank=True)
    last_name = models.CharField("Фамилия", max_length=255, blank=True)
    contry = models.CharField(
        verbose_name="Страна",
        max_length=255,
        blank=True
    )
    city = models.CharField(
        verbose_name="Город",
        max_length=255,
        blank=True
    )
    otp = models.CharField(max_length=6, null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "contry", "city"]

    class Meta:
        ordering = ("id",)
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
    
    def update(self, *args, **kwargs):
        number_list = [x for x in range(10)]  # Use of list comprehension
        code_items_for_otp = []

        for i in range(6):
            num = choice(number_list)
            code_items_for_otp.append(num)

        code_string = "".join(str(item) for item in code_items_for_otp)
        self.otp = code_string
        super().save(*args, **kwargs)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)