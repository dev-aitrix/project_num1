from django.db import models
from user.models import User
from product.models import Product
import uuid
# Create your models here.

class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)
    date_created = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    date_updated = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)
    order_sum = models.DecimalField( verbose_name='Сумма заказа', max_digits=12, decimal_places=2)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self) -> str:
        return self.id
    

class ProductOrder(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='product_order')
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_order')
    quantity = models.IntegerField()

    class Meta:
        verbose_name = 'Товар в заказе'
        verbose_name_plural = 'Товары в заказах'