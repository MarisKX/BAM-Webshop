from django.contrib import admin
from .models import (
    Category,
    ProductGroup,
    DesignCategory,
    ProductDesignGroup,
    Size,
    Color,
    Product,
    Design,
    Images,
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
        'relative_size',
    )


class ColorAdmin(admin.ModelAdmin):
    readonly_fields = ('name', )
    list_display = (
        'display_name',
        'name',
        'hex_code',
        'rgb_code',
    )


class DesignAdmin(admin.ModelAdmin):
    readonly_fields = ('name', )
    list_display = (
        'product_design_group',
        'product_design_category',
        'display_name',
        'name',
    )


class ImagesAdmin(admin.TabularInline):
    model = Images
    readonly_fields = ()
    list_display = (
        'image_url',
        'image',
    )


class ProductAdmin(admin.ModelAdmin):
    inlines = (ImagesAdmin,)
    readonly_fields = ('name', )
    list_display = (
        'product_group',
        'category',
        'design',
        'main_code',
        'sec_code',
        'code',
        'display_name',
        'name',
        'description',
        'size',
        'color',
        'price',
    )
    ordering = ('main_code',)


admin.site.register(ProductGroup, ProductGroupAdmin)
admin.site.register(ProductDesignGroup, ProductDesignGroupAdmin)
admin.site.register(Size, SizeAdmin)
admin.site.register(Color, ColorAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Design, DesignAdmin)
