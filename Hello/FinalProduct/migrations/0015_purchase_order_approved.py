# Generated by Django 2.2.3 on 2019-08-26 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FinalProduct', '0014_auto_20190728_0901'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase_order',
            name='Approved',
            field=models.BooleanField(default=False),
        ),
    ]
