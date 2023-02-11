from django.db import models
from .managers import CustomUserManager
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from school.models import Branch
from django.urls import reverse
# Create your models here.

class CustomUser(AbstractUser):
    user_code = models.CharField(_("Staff ID"), max_length=50)
    username = None
    email = models.EmailField(_("Email Address"), max_length=254, unique=True)
    customer_branch = models.ForeignKey(Branch, verbose_name=_("Branch"), on_delete=models.CASCADE, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = _("CustomUser")
        verbose_name_plural = _("CustomUsers")

    def __str__(self):
        return self.email

    
