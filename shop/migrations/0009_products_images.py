# Generated by Django 3.2.6 on 2022-11-12 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_remove_products_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='images',
            field=models.ManyToManyField(to='shop.ProductImages'),
        ),
    ]
