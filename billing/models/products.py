from uuid import uuid4

from django.db import models

from utils.helpers import get_random_string


class Product(models.Model):
    external_id = models.UUIDField(default=uuid4, unique=True, db_index=True)
    url = models.CharField(
        max_length=16, unique=True, db_index=True, blank=True, null=True
    )
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.url:
            self.url = get_random_string(8)
        return super().save(*args, **kwargs)
