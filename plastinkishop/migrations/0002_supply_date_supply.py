# Generated by Django 5.0.4 on 2024-04-18 05:57

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plastinkishop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='supply',
            name='date_supply',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Дата поставки'),
            preserve_default=False,
        ),
    ]
