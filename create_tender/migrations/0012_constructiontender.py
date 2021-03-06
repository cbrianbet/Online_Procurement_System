# Generated by Django 2.1.4 on 2019-06-14 13:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('create_tender', '0011_auto_20190614_1536'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConstructionTender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Model', models.CharField(max_length=80)),
                ('Net_power', models.CharField(max_length=80)),
                ('Electric', models.CharField(max_length=80)),
                ('Engine', models.CharField(default='No', max_length=80)),
                ('Operating_weight', models.CharField(max_length=80)),
                ('Certification', models.CharField(max_length=80)),
                ('Quantity', models.PositiveIntegerField()),
                ('tender_award', models.CharField(default='No', max_length=10)),
                ('date_created', models.DateField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date_created'],
            },
        ),
    ]
