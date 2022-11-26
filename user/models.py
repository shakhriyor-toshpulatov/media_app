from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class UserRoleChoices(models.TextChoices):
    ADMIN = 'Admin', 'Admin'
    SINGER = 'singer', 'singer'
    LISTENER = 'listener', 'listener'


class User(AbstractUser, models.Model):
    role = models.CharField(max_length=50, choices=UserRoleChoices.choices, blank=True, null=True)
    phone_number = models.CharField(max_length=100, blank=True, null=True)
    is_deleted = models.BooleanField(default=False)

    REQUIRED_FIELDS = ['role']


class Follower(models.Model):
    """ Модель подписчиков
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    subscriber = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscribers')

    def __str__(self):
        return f'{self.subscriber} подписан на {self.user}'


class SocialLink(models.Model):
    """ Модель ссылок на соц. сети пользователя
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='social_links')
    link = models.URLField(max_length=100)

    def __str__(self):
        return f'{self.user}'
