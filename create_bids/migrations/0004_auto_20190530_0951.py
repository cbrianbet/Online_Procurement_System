# Generated by Django 2.1.4 on 2019-05-30 06:51

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('create_bids', '0003_auto_20190526_2021'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bids',
            options={'ordering': ['-Bid_created_date']},
        ),
        migrations.AlterField(
            model_name='bids',
            name='Bid_documents_url',
            field=models.FileField(storage=django.core.files.storage.FileSystemStorage(location='/media/doc'), upload_to=''),
        ),
    ]
