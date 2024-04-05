from uuid import uuid4

from django.db import models
from django.contrib.postgres.fields import ArrayField


from utils.helpers import get_random_string

from billing.models import Product, Customer, User


class Bill(models.Model):
    external_id = models.UUIDField(default=uuid4, unique=True, db_index=True)
    url = models.CharField(
        max_length=16, unique=True, db_index=True, blank=True, null=True
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    orders = ArrayField(models.JSONField(), default=list)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    employee = models.ForeignKey(User, on_delete=models.PROTECT)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"Bill of {self.amount}"

    def save(self, *args, **kwargs) -> None:
        if not self.url:
            unique_id = get_random_string(8)
            while self.__class__.objects.filter(url=unique_id):
                unique_id = get_random_string(8)
            self.url = unique_id

        return super().save(*args, **kwargs)