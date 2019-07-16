# Generated by Django 2.2.3 on 2019-07-02 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Components',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Model_name', models.CharField(max_length=50)),
                ('Part_name', models.CharField(max_length=50)),
                ('Part_Number', models.IntegerField()),
                ('Primary_Stock_Unit', models.IntegerField()),
                ('Purchase_Stock_Unit', models.IntegerField()),
                ('Material', models.CharField(max_length=50)),
                ('type_of_production', models.CharField(max_length=50)),
                ('cost', models.IntegerField()),
                ('document', models.FileField(upload_to='documents/')),
            ],
        ),
        migrations.CreateModel(
            name='Process',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Finalproduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('component_list', models.ManyToManyField(to='FinalProduct.Components')),
            ],
        ),
    ]
