# Generated by Django 4.0.4 on 2022-05-10 14:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_images_remove_sizes_product_remove_sizes_size_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='images',
            options={'verbose_name_plural': 'Product Images'},
        ),
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image_url',
        ),
    ]
