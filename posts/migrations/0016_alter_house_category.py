# Generated by Django 5.0.7 on 2024-09-11 10:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0015_remove_house_carousel_house_category_houseimage_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='posts.category'),
        ),
    ]
