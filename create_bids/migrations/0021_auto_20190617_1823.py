# Generated by Django 2.1.4 on 2019-06-17 15:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('create_bids', '0020_auto_20190617_1821'),
    ]

    operations = [
        migrations.RenameField(
            model_name='desktopbid',
            old_name='bid_user',
            new_name='user',
        ),
    ]
