# Generated by Django 3.2.9 on 2021-12-23 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='inquiry',
            name='listing_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inquiry',
            name='user_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
