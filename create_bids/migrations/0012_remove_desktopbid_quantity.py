# Generated by Django 2.1.4 on 2019-06-14 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('create_bids', '0011_desktopbid_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='desktopbid',
            name='quantity',
        ),
    ]