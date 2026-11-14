from django.contrib import admin
from bela_moda.models import Brand, Product


class BrandAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "brand", "size", "price", "stock")
    search_fields = ("name",)
    list_filter = ("brand", "size")


admin.site.register(Brand, BrandAdmin)
admin.site.register(Product, ProductAdmin)
# Register your models here.
