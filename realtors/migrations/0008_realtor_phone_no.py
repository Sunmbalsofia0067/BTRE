# Generated by Django 3.2.9 on 2021-12-05 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0007_alter_realtor_hired_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='realtor',
            name='phone_no',
            field=models.CharField(default=123456789, max_length=15),
            preserve_default=False,
        ),
    ]
