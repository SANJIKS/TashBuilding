# Generated by Django 5.0.7 on 2024-10-07 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0036_comlstk_image_mobile'),
    ]

    operations = [
        migrations.AddField(
            model_name='navbaritem',
            name='link',
            field=models.CharField(blank=True, null=True),
        ),
    ]