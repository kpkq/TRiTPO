# Generated by Django 3.1 on 2020-08-09 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0004_auto_20200717_1910'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='null-slug'),
        ),
    ]
