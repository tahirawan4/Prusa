from django.contrib import admin

from products.models import Product, Category, ProductImage, CustomContent


class ProductImageInline(admin.StackedInline):
    model = ProductImage


class CustomContentInline(admin.StackedInline):
    model = CustomContent


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'product_type', 'price', 'stock', 'available', 'created_at', 'updated_at']
    list_filter = ['available', 'created_at', 'updated_at', 'product_type']
    list_editable = ['price', 'stock', 'available']
    inlines = [ProductImageInline, CustomContentInline]


admin.site.register(Category, CategoryAdmin)

admin.site.register(Product, ProductAdmin)
