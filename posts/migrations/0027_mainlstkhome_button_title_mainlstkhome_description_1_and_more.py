# Generated by Django 5.0.7 on 2024-10-05 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0026_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainlstkhome',
            name='button_title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='mainlstkhome',
            name='description_1',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mainlstkhome',
            name='description_2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mainlstkhome',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
