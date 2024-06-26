# Generated by Django 4.2.11 on 2024-04-05 02:50

import django.core.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0002_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_id', models.UUIDField(db_index=True, default=uuid.uuid4, unique=True)),
                ('url', models.CharField(blank=True, db_index=True, max_length=16, null=True, unique=True)),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', models.CharField(blank=True, max_length=15, null=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+918888888888'.", regex='^\\+?91?[6789]\\d{9}$')])),
                ('address', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
