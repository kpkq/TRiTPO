# Generated by Django 3.0.8 on 2020-07-17 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0003_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='prods/'),
        ),
    ]
