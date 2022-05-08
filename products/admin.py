from django.contrib import admin
from .models import (
    Category,
    ProductGroup,
    DesignCategory,
    ProductDesignGroup,
    Size,
    Color,
    Product,
)


class CategoryAdmin(admin.TabularInline):
    model = Category
    readonly_fields = ('name', )
    list_display = (
        'product_group',
        'display_name',
        'name',
    )


class ProductGroupAdmin(admin.ModelAdmin):
    inlines = (CategoryAdmin,)
    readonly_fields = ('name', )
    list_display = (
        'display_name',
        'name',
    )


class DesignCategoryAdmin(admin.TabularInline):
    model = DesignCategory
    readonly_fields = ('name', )
    list_display = (
        'product_design_group',
        'display_name',
        'name',
    )


class ProductDesignGroupAdmin(admin.ModelAdmin):
    inlines = (DesignCategoryAdmin,)
    readonly_fields = ('name', )
    list_display = (
        'display_name',
        'name',
    )


class SizeAdmin(admin.ModelAdmin):
    readonly_fields = ('name', )
    list_display = (
        'display_name',
        'name',
    )


class ColorAdmin(admin.ModelAdmin):
    readonly_fields = ('name', )
    list_display = (
        'display_name',
        'name',
    )


class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('name', )
    list_display = (
        'product_group',
        'category',
        'code',
        'display_name',
        'name',
        'description',
        'size',
        'color',
        'price',
    )


admin.site.register(ProductGroup, ProductGroupAdmin)
admin.site.register(ProductDesignGroup, ProductDesignGroupAdmin)
admin.site.register(Size, SizeAdmin)
admin.site.register(Color, ColorAdmin)
