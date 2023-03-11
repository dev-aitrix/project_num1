# Generated by Django 4.1.7 on 2023-03-07 11:03

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=20, verbose_name='имя')),
                ('last_name', models.CharField(max_length=30, verbose_name='фамилия')),
                ('e_mail', models.EmailField(max_length=254, verbose_name='email')),
                ('password', models.CharField(max_length=20, verbose_name='пароль')),
                ('address', models.CharField(max_length=200, verbose_name='адрес')),
                ('phone_number', models.CharField(max_length=30, verbose_name='номер телефона')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
    ]
