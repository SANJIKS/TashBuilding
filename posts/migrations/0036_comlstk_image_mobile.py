# Generated by Django 5.0.7 on 2024-10-07 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0035_alter_category_options_alter_footer_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comlstk',
            name='image_mobile',
            field=models.ImageField(blank=True, null=True, upload_to='posts/'),
        ),
    ]