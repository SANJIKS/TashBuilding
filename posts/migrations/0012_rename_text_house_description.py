# Generated by Django 5.0.7 on 2024-09-10 10:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0011_housecarousel_house'),
    ]

    operations = [
        migrations.RenameField(
            model_name='house',
            old_name='text',
            new_name='description',
        ),
    ]
