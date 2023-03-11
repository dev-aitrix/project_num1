from django.contrib import admin
from .models import Order, ProductOrder

# Register your models here.

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'date_created', 'date_updated', 'order_sum',)
    search_fields = ('user_id__email',)

@admin.register(ProductOrder)
class ProductOrderAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'product_id', 'quantity',)
    search_fields = ('product_id__product_name',)