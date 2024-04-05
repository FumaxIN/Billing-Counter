from uuid import uuid4
from django.db import models
from django.core.validators import RegexValidator

from utils.helpers import get_random_string

phone_regex = RegexValidator(
    regex=r"^[6789]\d{9}$",
    message="Phone number must be 10 digits and start with '6', '7', '8', or '9'.",
)


class Customer(models.Model):
    external_id = models.UUIDField(default=uuid4, unique=True, db_index=True)
    url = models.CharField(
        max_length=16, unique=True, db_index=True, blank=True, null=True
    )
    name = models.CharField(max_length=150, blank=False, null=False)
    email = models.EmailField(max_length=254, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True, validators=[phone_regex])
    address = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs) -> None:
        self.name = self.name.title()
        if not self.url:
            unique_id = get_random_string(8)
            while self.__class__.objects.filter(url=unique_id):
                unique_id = get_random_string(8)
            self.url = unique_id

        return super().save(*args, **kwargs)
