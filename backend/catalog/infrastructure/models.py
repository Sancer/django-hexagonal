from django.db import models

from shared.infrastructure.models import BaseModel


class Product(BaseModel):
    name = models.CharField(max_length=254)
    description = models.TextField()
