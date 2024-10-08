# Generated by Django 5.0.7 on 2024-10-05 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0029_bigdescription'),
    ]

    operations = [
        migrations.CreateModel(
            name='Technologically',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=120, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('button_title', models.CharField(blank=True, max_length=200, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='posts/')),
            ],
        ),
    ]
