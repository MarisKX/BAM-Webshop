# Generated by Django 4.0.4 on 2022-05-08 18:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_color_hex_code_color_rgb_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='color',
            name='rgb_code',
            field=models.CharField(max_length=11, unique=True, validators=[django.core.validators.MinLengthValidator(5)]),
        ),
    ]
