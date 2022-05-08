from django.db import models
from django.core.validators import (
    MaxValueValidator,
    MinValueValidator,
    MinLengthValidator,
)


# Create your models here.
class ProductGroup(models.Model):
    name = models.CharField(max_length=254)
    display_name = models.CharField(max_length=254, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Product Groups and Categories'

    def __str__(self):
        return self.name

    def get_display_name(self):
        return self.display_name

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the name.
        """
        self.name = self.display_name.replace(" ", "_").lower()
        super().save(*args, **kwargs)


class Category(models.Model):
    product_group = models.ForeignKey(ProductGroup, null=True, blank=False, on_delete=models.CASCADE, related_name='product_group')
    name = models.CharField(max_length=254)
    display_name = models.CharField(max_length=254, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_display_name(self):
        return self.display_name

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the name.
        """
        self.name = self.display_name.replace(" ", "_").lower()
        super().save(*args, **kwargs)


class ProductDesignGroup(models.Model):
    name = models.CharField(max_length=254)
    display_name = models.CharField(max_length=254, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Design Groups and Categories'

    def __str__(self):
        return self.name

    def get_display_name(self):
        return self.display_name

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the name.
        """
        self.name = self.display_name.replace(" ", "_").lower()
        super().save(*args, **kwargs)


class DesignCategory(models.Model):
    product_design_group = models.ForeignKey(ProductDesignGroup, null=True, blank=False, on_delete=models.CASCADE, related_name='product_design_group')
    name = models.CharField(max_length=254)
    display_name = models.CharField(max_length=254, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Design Categories'

    def __str__(self):
        return self.name

    def get_display_name(self):
        return self.display_name

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the name.
        """
        self.name = self.display_name.replace(" ", "_").lower()
        super().save(*args, **kwargs)


class Size(models.Model):
    name = models.CharField(max_length=254)
    display_name = models.CharField(max_length=254, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Product Sizes'

    def __str__(self):
        return self.name

    def get_display_name(self):
        return self.display_name

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the name.
        """
        self.name = self.display_name.replace(" ", "_").lower()
        super().save(*args, **kwargs)

    
class Color(models.Model):
    name = models.CharField(max_length=254)
    display_name = models.CharField(max_length=254, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Product Colors'

    def __str__(self):
        return self.name

    def get_display_name(self):
        return self.display_name

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the name.
        """
        self.name = self.display_name.replace(" ", "_").lower()
        super().save(*args, **kwargs)


class Product(models.Model):
    product_group = models.ForeignKey('ProductGroup', null=False, blank=False, on_delete=models.CASCADE)
    category = models.ForeignKey('Category', null=False, blank=False, on_delete=models.CASCADE)
    ean_code = models.CharField(max_length=13, validators=[MinLengthValidator(13)], unique=True, null=False, blank=False)
    size = models.ForeignKey('Size', null=False, blank=False, on_delete=models.CASCADE)
    color = models.ForeignKey('Color', null=False, blank=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
