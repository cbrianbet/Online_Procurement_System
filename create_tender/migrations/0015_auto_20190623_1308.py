# Generated by Django 2.1.4 on 2019-06-23 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('create_tender', '0014_furnituretender'),
    ]

    operations = [
        migrations.AddField(
            model_name='constructiontender',
            name='is_active',
            field=models.CharField(default='Yes', max_length=10),
        ),
        migrations.AddField(
            model_name='desktop_tender',
            name='is_active',
            field=models.CharField(default='Yes', max_length=10),
        ),
        migrations.AddField(
            model_name='furnituretender',
            name='is_active',
            field=models.CharField(default='Yes', max_length=10),
        ),
    ]