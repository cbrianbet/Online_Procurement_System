# Generated by Django 2.1.4 on 2019-06-14 09:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('create_tender', '0006_tender_tender_award'),
    ]

    operations = [
        migrations.CreateModel(
            name='Desktop_Tender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product', models.CharField(max_length=120)),
                ('Processor', models.CharField(max_length=120)),
                ('Operating_system', models.CharField(max_length=80)),
                ('Memory', models.CharField(max_length=100)),
                ('Storage', models.CharField(max_length=100)),
                ('Graphics', models.CharField(max_length=100)),
                ('tender_award', models.CharField(default='No', max_length=10)),
                ('date_created', models.DateField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='tender',
            name='tender_value',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
