# Generated by Django 4.0.4 on 2022-05-08 17:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_productgroup_category_product_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductDesignGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('display_name', models.CharField(blank=True, max_length=254, null=True)),
            ],
            options={
                'verbose_name_plural': 'Design Groups and Categories',
            },
        ),
        migrations.AlterModelOptions(
            name='productgroup',
            options={'verbose_name_plural': 'Product Groups and Categories'},
        ),
        migrations.CreateModel(
            name='DesignCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('display_name', models.CharField(blank=True, max_length=254, null=True)),
                ('product_design_group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_design_group', to='products.productdesigngroup')),
            ],
            options={
                'verbose_name_plural': 'Design Categories',
            },
        ),
    ]
