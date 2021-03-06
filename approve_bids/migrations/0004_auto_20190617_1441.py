# Generated by Django 2.1.4 on 2019-06-17 11:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('approve_bids', '0003_acceptconstbid_acceptfurnbid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acceptbid',
            name='bid_ID',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='create_bids.DesktopBid'),
        ),
        migrations.AlterField(
            model_name='acceptconstbid',
            name='bid_ID',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='create_bids.FurnitureBid'),
        ),
        migrations.AlterField(
            model_name='acceptfurnbid',
            name='bid_ID',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='create_bids.ConstructionBid'),
        ),
    ]
