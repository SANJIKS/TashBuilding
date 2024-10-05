# Generated by Django 5.0.7 on 2024-10-05 10:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0034_navbar_navbaritem'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='footer',
            options={'verbose_name': 'Футер', 'verbose_name_plural': 'Футеры'},
        ),
        migrations.AlterModelOptions(
            name='maincard',
            options={'verbose_name': 'Основная карта', 'verbose_name_plural': 'Основные карты'},
        ),
        migrations.AlterModelOptions(
            name='maincarditem',
            options={'verbose_name': 'Элемент карты', 'verbose_name_plural': 'Элементы карт'},
        ),
        migrations.AlterModelOptions(
            name='maincarousel',
            options={'verbose_name': 'Карусель', 'verbose_name_plural': 'Карусели'},
        ),
        migrations.AlterModelOptions(
            name='maincarouselitem',
            options={'verbose_name': 'Элемент карусели', 'verbose_name_plural': 'Элементы карусели'},
        ),
        migrations.AlterModelOptions(
            name='mainimage',
            options={'verbose_name': 'Основное изображение', 'verbose_name_plural': 'Основные изображения'},
        ),
        migrations.AlterModelOptions(
            name='mainlstkhome',
            options={'verbose_name': 'Дом LSTK', 'verbose_name_plural': 'Дома LSTK'},
        ),
        migrations.AlterModelOptions(
            name='size',
            options={'verbose_name': 'Размер', 'verbose_name_plural': 'Размеры'},
        ),
        migrations.AlterModelOptions(
            name='sizecarousel',
            options={'verbose_name': 'Карусель размеров', 'verbose_name_plural': 'Карусели размеров'},
        ),
        migrations.AlterModelOptions(
            name='sizecarouselimage',
            options={'verbose_name': 'Изображение карусели', 'verbose_name_plural': 'Изображения карусели'},
        ),
        migrations.AlterField(
            model_name='sizecarouselimage',
            name='size',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='items', to='posts.size'),
        ),
    ]
