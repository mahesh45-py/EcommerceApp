# Generated by Django 3.2.6 on 2022-11-13 13:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_auto_20221112_2118'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=16)),
                ('phone', models.IntegerField()),
                ('password', models.CharField(max_length=16)),
                ('status', models.CharField(choices=[('AC', 'Active'), ('BL', 'Blocked')], default='AC', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField()),
                ('first_name', models.CharField(max_length=80)),
                ('last_name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('country', models.CharField(max_length=80)),
                ('state', models.CharField(max_length=80)),
                ('zip', models.IntegerField()),
                ('address1', models.TextField()),
                ('address2', models.TextField()),
                ('status', models.CharField(choices=[('IP', 'In Progress'), ('PS', 'Payment Success'), ('PF', 'Payment Failed'), ('PN', 'Payment Pending'), ('TS', 'Transit'), ('DL', 'Delevered')], default='PN', max_length=2)),
                ('provider_order_id', models.CharField(max_length=40)),
                ('payment_id', models.CharField(max_length=36)),
                ('signature_id', models.CharField(max_length=128)),
                ('products', models.ManyToManyField(to='shop.Products')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.customer')),
            ],
        ),
    ]
