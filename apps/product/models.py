from django.db import models
import uuid
from order.models import Order

# Create your models here.

    
class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category_name = models.CharField(verbose_name='Категория', max_length=20)
    date_created = models.DateTimeField(verbose_name='Дата и время создания', auto_now_add=True)
    date_updated = models.DateTimeField(verbose_name='Дата и время обновления', auto_now=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self) -> str:
        return self.category

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product_name = models.CharField(verbose_name='Наименование товара', max_length=50)
    category = models.ForeignKey(Category, verbose_name='Категория', max_length=30, related_name='products', on_delete=models.CASCADE)
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(verbose_name='Цена', max_digits=12, decimal_places=2)
    quantity = models.IntegerField(verbose_name='Количество')
    date_added = models.DateTimeField(verbose_name='Дата и время добавления продукта', auto_now_add=True)
    date_updated = models.DateTimeField(verbose_name='Дата и время обновления', auto_now=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self) -> str:
        return self.product_name
