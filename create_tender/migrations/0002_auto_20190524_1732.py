# Generated by Django 2.1.4 on 2019-05-24 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('create_tender', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='createtender',
            name='tender_duration',
            field=models.PositiveIntegerField(default=10),
        ),
        migrations.AlterField(
            model_name='createtender',
            name='is_active',
            field=models.CharField(default=None, max_length=10),
        ),
    ]
