# Generated by Django 4.2.4 on 2023-08-29 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matching', '0007_userinfor_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfor',
            name='status',
            field=models.IntegerField(blank=True, default=2),
        ),
    ]
