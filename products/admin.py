
from django.contrib import admin
from .models import Product, Company

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'price', 'stock_quantity')
    search_fields = ('name', 'company__name')
    list_filter = ('company',)

admin.site.register(Company)
