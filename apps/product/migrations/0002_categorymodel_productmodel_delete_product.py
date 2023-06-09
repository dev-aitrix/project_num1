# Generated by Django 4.1.7 on 2023-03-14 13:55

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20, verbose_name='Категория')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Дата и время обновления')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, verbose_name='Наименование товара')),
                ('description', models.TextField(verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Цена')),
                ('quantity', models.IntegerField(verbose_name='Количество')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время добавления продукта')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Дата и время обновления')),
                ('category', models.ForeignKey(max_length=30, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='product.categorymodel', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
