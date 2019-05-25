# Generated by Django 2.1.4 on 2019-05-25 18:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('create_bids', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bids',
            name='User_ID',
        ),
        migrations.AddField(
            model_name='bids',
            name='user',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]