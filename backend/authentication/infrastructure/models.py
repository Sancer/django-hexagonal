from django.contrib.auth.models import AbstractUser

from shared.infrastructure.models import BaseModel, BaseManager
from django.contrib.auth.models import UserManager


class BaseUserManager(BaseManager, UserManager):
    pass


class User(BaseModel, AbstractUser):
    objects = BaseUserManager()
    all_objects = UserManager()
