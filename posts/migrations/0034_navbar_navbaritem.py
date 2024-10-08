# Generated by Django 5.0.7 on 2024-10-05 08:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0033_remove_footer_instagram_remove_footer_telegram_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Navbar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=120, null=True)),
                ('link_inst', models.CharField(blank=True, max_length=200, null=True)),
                ('link_youtube', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='NavbarItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, null=True)),
                ('navbar', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='items', to='posts.navbar')),
            ],
        ),
    ]
