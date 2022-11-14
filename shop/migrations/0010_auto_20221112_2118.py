# Generated by Django 3.2.6 on 2022-11-12 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_products_images'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.DeleteModel(
            name='ProductImages',
        ),
        migrations.AlterField(
            model_name='products',
            name='images',
            field=models.ManyToManyField(to='shop.ProductImage'),
        ),
    ]