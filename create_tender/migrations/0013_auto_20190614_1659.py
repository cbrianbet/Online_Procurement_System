# Generated by Django 2.1.4 on 2019-06-14 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('create_tender', '0012_constructiontender'),
    ]

    operations = [
        migrations.RenameField(
            model_name='constructiontender',
            old_name='Model',
            new_name='Mod',
        ),
    ]