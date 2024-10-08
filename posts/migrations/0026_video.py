# Generated by Django 5.0.7 on 2024-09-30 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0025_advantage_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(blank=True, max_length=300, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='posts')),
                ('text', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
