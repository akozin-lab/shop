# Generated by Django 3.1.2 on 2020-12-11 14:56

from django.db import migrations, models
import onlineshop.models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineshop', '0010_auto_20201206_2020'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shippingaddress',
            name='town',
        ),
        migrations.AlterField(
            model_name='page',
            name='product',
            field=models.CharField(max_length=200, null=True, verbose_name=onlineshop.models.Product),
        ),
    ]