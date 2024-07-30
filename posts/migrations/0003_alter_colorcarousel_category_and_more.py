# Generated by Django 5.0.7 on 2024-07-30 12:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_colorcarouselitem_carousel_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colorcarousel',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='color_carousels', to='posts.category'),
        ),
        migrations.AlterField(
            model_name='maincarousel',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='main_carousels', to='posts.category'),
        ),
    ]
