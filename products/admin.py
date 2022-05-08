from django.contrib import admin
from .models import (
    Category,
    ProductGroup,
    DesignCategory,
    ProductDesignGroup,
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


admin.site.register(ProductGroup, ProductGroupAdmin)
admin.site.register(ProductDesignGroup, ProductDesignGroupAdmin)
