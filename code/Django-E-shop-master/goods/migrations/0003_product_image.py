# Generated by Django 3.0.8 on 2020-07-17 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_product_prod_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
