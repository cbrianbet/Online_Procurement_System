# Generated by Django 2.1.4 on 2019-05-14 17:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='bio',
            new_name='ac_type',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='location',
            new_name='comp_name',
        ),
    ]
