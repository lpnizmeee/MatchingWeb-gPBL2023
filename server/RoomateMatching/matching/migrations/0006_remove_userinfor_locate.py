# Generated by Django 4.2.4 on 2023-08-29 05:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matching', '0005_userinfor_locate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfor',
            name='locate',
        ),
    ]
