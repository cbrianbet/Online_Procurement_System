# Generated by Django 2.1.4 on 2019-06-15 09:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('create_bids', '0016_auto_20190614_2349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='constructionbid',
            name='Tender_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='create_tender.ConstructionTender'),
        ),
        migrations.AlterField(
            model_name='furniturebid',
            name='Tender_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='create_tender.FurnitureTender'),
        ),
    ]
