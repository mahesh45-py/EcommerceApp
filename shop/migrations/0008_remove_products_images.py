# Generated by Django 3.2.6 on 2022-11-12 15:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_remove_productimages_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='images',
        ),
    ]