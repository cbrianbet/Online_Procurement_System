# Generated by Django 2.1.4 on 2019-06-17 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('create_bids', '0019_auto_20190617_1636'),
    ]

    operations = [
        migrations.RenameField(
            model_name='desktopbid',
            old_name='user',
            new_name='bid_user',
        ),
    ]
