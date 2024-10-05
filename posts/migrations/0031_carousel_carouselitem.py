# Generated by Django 5.0.7 on 2024-10-05 08:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0030_technologically'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=120, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CarouselItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=120, null=True)),
                ('size', models.CharField(blank=True, max_length=120, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='posts/')),
                ('carousel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='carousels', to='posts.carousel')),
            ],
        ),
    ]
