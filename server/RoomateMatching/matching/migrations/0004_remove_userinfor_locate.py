# Generated by Django 4.2.4 on 2023-08-28 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matching', '0003_userinfor_latitude_userinfor_longtitude_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfor',
            name='locate',
        ),
    ]