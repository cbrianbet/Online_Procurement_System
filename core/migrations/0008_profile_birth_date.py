# Generated by Django 2.1.4 on 2019-05-20 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20190519_1419'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='birth_date',
            field=models.DateField(auto_now=True),
        ),
    ]
