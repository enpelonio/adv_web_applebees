# Generated by Django 3.1.1 on 2020-10-08 06:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_auto_20201008_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='birthdate',
            field=models.DateField(default=datetime.datetime(2020, 10, 8, 14, 58, 31, 847114)),
        ),
        migrations.AlterField(
            model_name='person',
            name='dateregistered',
            field=models.DateField(default=datetime.datetime(2020, 10, 8, 14, 58, 31, 847114)),
        ),
        migrations.AlterField(
            model_name='product',
            name='datereg',
            field=models.DateField(default=datetime.datetime(2020, 10, 8, 14, 58, 31, 846127)),
        ),
    ]
