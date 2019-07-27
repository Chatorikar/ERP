# Generated by Django 2.2.3 on 2019-07-27 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FinalProduct', '0011_auto_20190719_2042'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('company_name', models.CharField(max_length=50)),
                ('email_id', models.CharField(max_length=60)),
                ('phone_no', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Purchase_Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=50)),
                ('Final_Product_list', models.ManyToManyField(to='FinalProduct.Finalproduct')),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='members', to='FinalProduct.Customer')),
            ],
        ),
    ]
