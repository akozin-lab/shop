# Generated by Django 3.1.2 on 2020-12-06 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onlineshop', '0008_pages'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='pages',
            new_name='Page',
        ),
    ]