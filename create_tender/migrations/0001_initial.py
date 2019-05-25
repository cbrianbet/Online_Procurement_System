# Generated by Django 2.1.4 on 2019-05-20 11:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0008_profile_birth_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreateTender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tender_title', models.CharField(max_length=64)),
                ('tender_desc', models.CharField(max_length=500)),
                ('date_created', models.DateField(auto_now=True)),
                ('is_active', models.BooleanField(default=None)),
                ('tender_value', models.PositiveIntegerField()),
                ('seller_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Profile')),
            ],
        ),
    ]