# Generated by Django 3.2.9 on 2021-12-04 19:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0004_alter_realtor_hired_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtor',
            name='hired_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 4, 11, 44, 43, 285234)),
        ),
    ]
