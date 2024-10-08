# Generated by Django 5.0.7 on 2024-08-08 09:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_footer'),
    ]

    operations = [
        migrations.CreateModel(
            name='SizeCarouselImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='posts/')),
                ('number', models.PositiveSmallIntegerField(default=0)),
                ('size', models.CharField(blank=True, max_length=120, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='colorcarouselimage',
            name='color',
        ),
        migrations.RenameModel(
            old_name='ColorCarousel',
            new_name='SizeCarousel',
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(blank=True, max_length=200, null=True)),
                ('carousel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='items', to='posts.sizecarousel')),
            ],
        ),
        migrations.DeleteModel(
            name='Color',
        ),
        migrations.DeleteModel(
            name='ColorCarouselImage',
        ),
    ]
