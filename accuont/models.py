from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

from .manager import UserManager


class User(AbstractBaseUser):
    image           = models.ImageField(upload_to="user_images/", default="user_images/default.png")
    full_name       = models.CharField(max_length=30)
    date_of_birth   = models.DateField(null=True, blank=True, default=None)
    adress          = models.CharField(max_length=255, null=True, blank=True, default=None)
    user_name       = models.CharField(max_length=20, unique=True)
    national_code   = models.CharField(max_length=10, unique=True, null=True, blank=True, default=None)
    phone           = models.CharField(max_length=11, unique=True)
    is_active       = models.BooleanField(default=True)
    is_admin        = models.BooleanField(default=False)
    date_joined     = models.DateField(auto_now_add=True)
    objects = UserManager()

    USERNAME_FIELD = "user_name"
    REQUIRED_FIELDS = ["full_name","phone", "adress"]

    def __str__(self):
        return self.full_name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

