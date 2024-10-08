# Generated by Django 5.0.7 on 2024-07-31 11:35

import colorfield.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_alter_colorcarousel_category_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', colorfield.fields.ColorField(default='#FF0000', image_field=None, max_length=25, samples=None)),
                ('carousel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='items', to='posts.colorcarousel')),
            ],
        ),
        migrations.CreateModel(
            name='ColorCarouselImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='posts/')),
                ('number', models.PositiveSmallIntegerField(default=0)),
                ('size', models.CharField(blank=True, max_length=120, null=True)),
                ('color', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='items', to='posts.color')),
            ],
        ),
        migrations.DeleteModel(
            name='ColorCarouselItem',
        ),
    ]
