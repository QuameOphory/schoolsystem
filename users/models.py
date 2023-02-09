from django.db import models
from .managers import CustomUserManager
from django.urls import reverse
# Create your models here.

class CustomUser(models.Model):

    username = None
    email = models.EmailField(_("Email Address"), max_length=254, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = _("CustomUser")
        verbose_name_plural = _("CustomUsers")

    def __str__(self):
        return self.email

